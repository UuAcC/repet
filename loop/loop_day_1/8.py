c = 0
for q in ['А', "О", "У"]:
    for w in ['А', "О", "У"]:
        for e in ['А', "О", "У"]:
            for r in ['А', "О", "У"]:
                for t in ['А', "О", "У"]:
                    c += 1
                    print(f'{q}{w}{e}{r}{t}', c)
