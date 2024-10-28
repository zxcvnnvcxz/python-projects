def mergeTwoLists(List1, List2):
    merged = []
    i = 0
    x, y = 0, 0
    for i in list1:
        x += 1
    for i in list2:
        y += 1

    if not List1 and not List2:
        return merged

    if not List1 and List2:
        merged = List2
        return merged

    if not List2 and List1:
        merged = List1
        return merged

    while i < x or i < y:
        if List1[i] >= List2[i]:
            merged.append(List2[i])
            merged.append(List1[i])
            i += 1
        else:
            merged.append(List1[i])
            merged.append(List2[i])
            i += 1
    return merged

if __name__ == "__main__":
    list1 = []
    list2 = [0]
    print(mergeTwoLists(list1, list2))