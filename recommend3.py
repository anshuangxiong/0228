from collections import defaultdict
import math
import operator





def read_data(data_path, sep):
    fp = open(data_path, "r")
    user2item_matrix = defaultdict(defaultdict)  # 用户到物品的评分矩阵
    item2user_matrix = defaultdict(defaultdict)  # 物品到用户的倒排评分矩阵
    # UserID \t MovieID \t Score \t Time
    for line in open(data_path):
        lines = line.strip().split(sep)
        userID, movieID, score = lines[0], lines[1], lines[2]
        user2item_matrix[userID][movieID] = float(score)
        item2user_matrix[movieID][userID] = float(score)
    fp.close()
    return user2item_matrix, item2user_matrix


def item_sim_cosine(item2user_matrix):

    W = defaultdict(defaultdict)  # 物品-物品-相似度矩阵
    item_list = item2user_matrix.keys()
    for i in item_list:
        for j in item_list:
            if i == j:
                continue
            W[i][j] = len(set(item2user_matrix[i].keys()) & set(item2user_matrix[j].keys())) # 交集
            W[i][j] /= math.sqrt(len(item2user_matrix[i].keys())*len(item2user_matrix[j].keys())*1.0)
            if W[i][j] != 0:
                f = open('item.txt', 'a+')
                f.write("(" + i + "," + j + ")    " + str(W[str(i)][str(j)]) + "\n")
                f.close()
    """
    f = open('item.txt', 'w')
    for i in W:
        for j in W:
            if i == j:
                continue
            f.write("("+i+","+j+")    "+str(W[str(i)][str(j)])+"\n")
    f.close()
    """
    print(W['1'])
    print(W['1']['2'])
    print(W['1'].items())
    return W



def recommend(user2item_matrix, user_id, W, K=10):
    '''通过用户userid、训练集数据、用户相似度矩阵进行topN推荐'''
    rank=defaultdict(int)
    # 获取用户的物品列表
    user_item_set = user2item_matrix[user_id].keys()

    # 遍历用户喜欢的物品列表
    for item, item_score in user2item_matrix[user_id].items():
        # 遍历与该物品相似的物品
        for w_itemid, w_score in sorted(W[item].items(), key=operator.itemgetter(1), reverse=True)[0:K]:
            # 如果相似用户看过的电影也在目标用户的物品集合中，则忽略该物品的推荐
            if w_itemid in user_item_set:
                continue
            # 计算该物品推荐给用户的排序分
            rank[w_itemid] = w_score * item_score
    # 对所有推荐物品与打分按照排序分进行降序排序，取前K个物品
    rank_list = sorted(rank.items(),key=operator.itemgetter(1),reverse=True)[0:K]
    return rank_list


if __name__ == "__main__":

    data_path = "data/ratings2.csv"
    sep = ","
    user2item_matrix, item2user_matrix = read_data(data_path, sep)
    W = item_sim_cosine(item2user_matrix)
    print(W)
    userId = input("请输入推荐的用户: ")
    recommendNum = input("请输入给用户"+userId+"推荐的数量: ")
    rank_list = recommend(user2item_matrix, str(userId), W, int(recommendNum))
    print(rank_list)
