def id_generator():
    count = 1
    while count >= 1:
        yield f"ID_{count}"
        count += 1
#initialize generator object
id_gen = id_generator()

# Testing the result
for _ in range(5):
    unique_id = next(id_gen)
    print(unique_id)