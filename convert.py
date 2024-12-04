import re
import argparse

# 读取 RIS 文件
def read_ris_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# 解析 RIS 文件，提取关键信息
def parse_ris_to_dict(ris_lines):
    references = []
    ref = {}
    for line in ris_lines:
        line = line.strip()
        
        if line.startswith('%0'):  # 开始新引用
            if ref:  # 保存上一个引用
                references.append(ref)
                ref = {}
        elif line.startswith('%A'):  # 作者
            authors = ref.get('authors', [])
            authors.append(line[2:].strip())
            ref['authors'] = authors
        elif line.startswith('%T'):  # 标题
            ref['title'] = line[2:].strip()
        elif line.startswith('%J'):  # 期刊名称
            ref['journal'] = line[2:].strip()
        elif line.startswith('%D'):  # 发表年份
            ref['year'] = line[2:].strip()
        elif line.startswith('%V'):  # 卷号
            ref['volume'] = line[2:].strip()
        elif line.startswith('%N'):  # 期号
            ref['issue'] = line[2:].strip()
        elif line.startswith('%P'):  # 页码
            ref['pages'] = line[2:].strip()
        elif line.startswith('%K'):  # 关键词
            ref['keywords'] = line[2:].strip()
        elif line.startswith('%X'):  # 摘要
            ref['abstract'] = line[2:].strip()
        elif line.startswith('%U'):  # URL
            ref['url'] = line[2:].strip()
        elif line.startswith('%R'):  # DOI
            ref['doi'] = line[2:].strip()

    # 保存最后一个引用
    if ref:
        references.append(ref)
    
    return references

# 将数据转换为 Neo4j 查询
def convert_to_neo4j_query(references):
    queries = []
    for ref in references:
        # 创建文献节点，包括 title, year, abstract, doi 和 url
        query = f"CREATE (p:Paper {{title: '{ref['title']}', publication_year: '{ref['year']}', abstract: '{ref.get('abstract', '')}', journal: '{ref.get('journal', '')}', doi: '{ref.get('doi', '')}', website_url: '{ref.get('url', '')}'}})"
        queries.append(query)


        # 创建作者节点并连接到文献节点
        for author in ref.get('authors', []):
            query = f"CREATE (a:Author {{name: '{author}'}}) "
            query += f"MERGE (r)-[:AUTHORED_BY]->(a)"
            queries.append(query)

        # 创建期刊节点并连接到文献节点
        # if 'journal' in ref:
        #    query = f"CREATE (j:Journal {{name: '{ref['journal']}'}}) "
        #    query += f"MERGE (r)-[:PUBLISHED_IN]->(j)"
        #    queries.append(query)

        # 创建卷号和期号节点并连接
        #if 'volume' in ref:
        #    query = f"CREATE (v:Volume {{number: '{ref['volume']}'}}) "
        #    query += f"MERGE (r)-[:PUBLISHED_IN]->(v)"
        #    queries.append(query)

        #if 'issue' in ref:
        #   query = f"CREATE (i:Issue {{number: '{ref['issue']}'}}) "
        #   query += f"MERGE (r)-[:PUBLISHED_IN]->(i)"
        #   queries.append(query)

        # 创建页码关系
        #if 'pages' in ref:
        #    query = f"MERGE (r)-[:PAGES {{range: '{ref['pages']}'}}]->(p:Pages)"
        #    queries.append(query)

        # 创建关键词节点并连接到文献节点
        if 'keywords' in ref:
            for keyword in ref.get('keywords', '').split(';'):
                query = f"MERGE (k:Keyword {{name: '{keyword.strip()}'}}) "
                query += f"MERGE (r)-[:HAS_KEYWORD]->(k)"
                queries.append(query)

    return queries

# 主函数，处理命令行参数
def main():
    parser = argparse.ArgumentParser(description="Convert RIS file to Neo4j queries.")
    parser.add_argument("ris_file", help="Path to the RIS file")
    args = parser.parse_args()

    # 读取 RIS 文件并转换为 Neo4j 查询
    ris_lines = read_ris_file(args.ris_file)
    references = parse_ris_to_dict(ris_lines)
    queries = convert_to_neo4j_query(references)
    
    # 输出 Neo4j 查询
    for query in queries:
        print(query)

# 执行主函数
if __name__ == "__main__":
    main()
