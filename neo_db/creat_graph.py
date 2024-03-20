from config import graph

# 生成人物节点和关系节点
with open("../raw_data/relation.txt") as f:
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        #  0     1      2      3          4
        # 人物1，人物2，关系， 人物1家族， 人物2家族
        # 贾演, 贾代化, 父亲, 贾家宁国府, 贾家宁国府
        try:
            # 生成人物1节点，附加属性：家族
            graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[3], rela_array[0]))
            # 生成人物2节点，附加属性：家族
            graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[1]))
            graph.run(
                "MATCH(e: Person), (cc: Person) \
                WHERE e.Name='%s' AND cc.Name='%s'\
                CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
                RETURN r" % (rela_array[0], rela_array[1], rela_array[2], rela_array[2])
            )
        except Exception as e:
            print("An error occurred while executing the Cypher query:", e)
