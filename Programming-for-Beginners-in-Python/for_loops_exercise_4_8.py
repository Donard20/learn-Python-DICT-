#for loops

furniture = ["table", "chair", "cabinet", "desk", "couch"]

for i in furniture:
    if i == "cabinet":          # -- conditional logic
        continue                # -- remove the cabinet in the list
    print(i)

# print table
# chair
# desk
# couch