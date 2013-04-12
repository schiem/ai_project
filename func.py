def instances_of(a, b):
    indices = []
    for i in range(0, len(b)):
        if a == b[i:i+len(a)]:
            indices.append(i)
            i += len(a)
    return indices
