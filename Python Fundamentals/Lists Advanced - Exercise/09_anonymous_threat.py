def merge_element(elements, start, end):
    merge_result = ""
    for i in range(start, end + 1):
        merge_result += elements[i]

    return merge_result


words = input().split()

while True:
    line = input()
    if line == "3:1":
        break
    command, first_arg, second_arg = line.split()
    if command == "merge":
        start_idx = int(first_arg)
        end_idx = int(second_arg)
        start_idx = max(0, start_idx)
        end_idx = min(len(words) - 1, end_idx)

        merged_element = merge_element(words, start_idx, end_idx)

    elif command == "divide":
        el_idx = int(first_arg)
        partitions = int(second_arg)
        element = words[el_idx]
        elements_parts = []
        partition_size = len(element) // partitions
        current_partition = ""
        for idx in range(partitions - 1):
            current_partition += element[idx]
            if len(current_partition) == partition_size:
                elements_parts.append(current_partition)
                current_partition = ""

print(" ".join(words))
