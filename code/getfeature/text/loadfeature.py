import torch
if __name__ == "__main__":
    data = torch.load('./tfidf_features/tfidf_features_part1.pt')

    print(data)
    print(type(data))
    print(len(data))
    print(data[0])
    print(type(data[0]))
    print(data[0].shape)

    # print(data[0].keys())
    # print(type(data[0]))
    # print(data[0]['file'])
    # print(data[0]['app'])
    # print(data[0]['scr'])
    # print(data[0]['extra'])
    # print(data[10]['tag'])
    # print(len(data))