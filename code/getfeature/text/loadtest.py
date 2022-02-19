import torch

if __name__ == "__main__":

    datapt = torch.load('data_guis_news.pt')
    #
    # for key in datapt[0][0].keys():
    #     print(key)
    print(datapt)
    #print(datapt[0][0]['tree'])


    print("img")
    print(datapt[0][5]['img'])
    print("vec")
    print(datapt[0][0]['vec'])
    print("title")
    print(datapt[0][0]['title'])
    print("file")
    print(datapt[0][1]['file'])
    print("app")
    print(datapt[0][1]['app'])
    print("scr")
    print(datapt[0][0]['scr'])
    print("extra")
    print(datapt[0][0]['extra'])
    print("tag")
    print(datapt[0][0]['tag'])

    for x in datapt[0]:
        if x['img']!= '':
            print(x['img'])