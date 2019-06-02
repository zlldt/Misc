import numpy as np
# 以1SR为单位
# SSR升技，所需技狗为当前技能等级*2SR
# SSR:SR = 10:1
costbase = [10, 1]
ssr_lvlup_cost = [2 * x for x in range(15)]
ssr_lvlup_cost_v1 = [0 for x in range(15)]
#detail数量 [SSR,SR]
ssr_basecost_detail_v1 = [[0, 0] for x in range(15)]
# 1SR等价1SR,1SSR等价10SR

ssr_lvlup_cost_v1[1] = 10
ssr_basecost_detail_v1[1] = [1, 0]
for x in range(2, 15):
    ssr_lvlup_cost_v1[x] = ssr_lvlup_cost_v1[x - 1] + 2 * (x - 1)
    ssr_basecost_detail_v1[x][0] = ssr_basecost_detail_v1[x - 1][0]
    ssr_basecost_detail_v1[x][1] = ssr_basecost_detail_v1[x -
                                                          1][1] + 2 * (x - 1)
# 只吃SR升级，获得x级技狗成本
print('只吃SR升技，获得x级技狗成本')
print('ssr_lvlup_cost_v1',ssr_lvlup_cost_v1)
print('ssr_basecost_detail_v1',ssr_basecost_detail_v1)

# 优化吃技狗成本，高于5级，所需技狗等于1SSR时，吃1SSR，大于等于12SR、小于22SR时，吃SSRlv2(1SSR+2SR)，大于等于24SR时，吃SSRlv3(1SSR+6SR)
for x in range(2, 15):
    # 5升6，吃SSRlv1
    if x == 6:
        ssr_lvlup_cost_v1[x] = ssr_lvlup_cost_v1[x - 1] + 10
        ssr_basecost_detail_v1[x][0] = ssr_basecost_detail_v1[x - 1][0] + 1
        ssr_basecost_detail_v1[x][1] = ssr_basecost_detail_v1[x - 1][1]
    # 6升7到10升11，吃SSRlv2
    if x > 6 and x < 12:
        ssr_lvlup_cost_v1[x] = ssr_lvlup_cost_v1[x - 1] + 12
        ssr_basecost_detail_v1[x][0] = ssr_basecost_detail_v1[x - 1][0] + 1
        ssr_basecost_detail_v1[x][1] = ssr_basecost_detail_v1[x - 1][1] + 2
    # 11升12，吃SSRlv2+2SR
    if x == 12:
        ssr_lvlup_cost_v1[x] = ssr_lvlup_cost_v1[x - 1] + 14
        ssr_basecost_detail_v1[x][0] = ssr_basecost_detail_v1[x - 1][0] + 1
        ssr_basecost_detail_v1[x][1] = ssr_basecost_detail_v1[x - 1][1] + 4
    # 12升13及以上，吃SSRlv3
    if x > 12:
        ssr_lvlup_cost_v1[x] = ssr_lvlup_cost_v1[x - 1] + 16
        ssr_basecost_detail_v1[x][0] = ssr_basecost_detail_v1[x - 1][0] + 1
        ssr_basecost_detail_v1[x][1] = ssr_basecost_detail_v1[x - 1][1] + 6
print('SSR吃SR及SSR升技，获得x级技狗成本')
print('ssr_lvlup_cost_v1',ssr_lvlup_cost_v1)
print('ssr_basecost_detail_v1',ssr_basecost_detail_v1)


# 巴武，SSR天司，x技能等级吃合计x等级的SSR升技能
bahamut_lvlup_cost = [10 * x for x in range(15)]
bahamut_basecost_detail = [[0, 0] for x in range(15)]
bahamut_basecost_detail_sum=[[0,0] for x in range(15)]
# 巴武吃SSR升级，统计SSR技能武器数量：[0,SSRlv1,SSRlv2,SSRlv3,SSRlv4,SSRlv5]
bahamut_ssr_list = [[0 for x in range(6)]for y in range(15)]
bahamut_ssr_list[0] = [0, 0, 0, 0, 0, 0]
bahamut_ssr_list[1] = [0, 1, 0, 0, 0, 0]
bahamut_ssr_list[2] = [0, 0, 1, 0, 0, 0]
bahamut_ssr_list[3] = [0, 0, 0, 1, 0, 0]
bahamut_ssr_list[4] = [0, 0, 0, 0, 1, 0]
bahamut_ssr_list[5] = [0, 0, 0, 0, 0, 1]
for x in range(5):
    bahamut_basecost_detail[x]=ssr_basecost_detail_v1[x]

for x in range(5, 15):
    #value1 = bahamut_basecost_detail[1][0] * 10 + bahamut_basecost_detail[1][1]
    value1 = np.dot(bahamut_basecost_detail[1], costbase)
    #value2 = bahamut_basecost_detail[x - 1][0] * 10 + bahamut_basecost_detail[x - 1][1]
    value2 = np.dot(bahamut_basecost_detail[x - 1], costbase)
    maxcost = value1 + value2
    for y in range(1, x):
        if y <= (x - y):
            #value1 = bahamut_basecost_detail[y][0] * 10 + bahamut_basecost_detail[y][1]
            value1 = np.dot(bahamut_basecost_detail[y], costbase)
            #value2 = bahamut_basecost_detail[x - y][0] * 10 + bahamut_basecost_detail[x - y][1]
            value2 = np.dot(bahamut_basecost_detail[x - y], costbase)
            currentcost = value1 + value2
            # print('Bahamut lvl:',x,'PartA:lvl ',y,'cost: ',value1,'PartB:lvl ',x-y,'cost: ',value2,'currentcost=',value1+value2,bahamut_lvlup_cost[x],maxcost)
            if currentcost<maxcost:
            # if value1 + value2 < cost:
            #     for z in range(6):
            #         bahamut_ssr_list[x][z] = bahamut_ssr_list[y][z] + bahamut_ssr_list[x - y][z]
                bahamut_ssr_list[x] = np.add(bahamut_ssr_list[y],bahamut_ssr_list[x - y])
                # bahamut_basecost_detail[x][0]=bahamut_basecost_detail[y][0]+bahamut_basecost_detail[x-y][0]
                # bahamut_basecost_detail[x][1]=bahamut_basecost_detail[y][1]+bahamut_basecost_detail[x-y][1]
                bahamut_basecost_detail[x] = np.add(bahamut_basecost_detail[y], bahamut_basecost_detail[x-y])
                # bahamut_lvlup_cost[x]=bahamut_basecost_detail[x][0]*10+bahamut_basecost_detail[x][1]
                maxcost = currentcost
            # print(x,bahamut_ssr_list[x],bahamut_basecost_detail[x])

#升技总成本
bahamut_basecost_detail_sum[0]=bahamut_basecost_detail[0]
bahamut_basecost_detail_sum[1]=bahamut_basecost_detail[1]
for x in range(2,15):
    bahamut_basecost_detail_sum[x][0]=bahamut_basecost_detail_sum[x-1][0]+bahamut_basecost_detail[x][0]
    bahamut_basecost_detail_sum[x][1]=bahamut_basecost_detail_sum[x-1][1]+bahamut_basecost_detail[x][1]
print('巴武，SSR天司升技能所需成本：SSR技能武器数量：[0,SSRlv1,SSRlv2,SSRlv3,SSRlv4,SSRlv5]')
print('bahamut_ssr_list',bahamut_ssr_list)
print('巴武，SSR天司升技能所需成本：SSR技能武器数量：[0,SSRlv1,SSRlv2,SSRlv3,SSRlv4,SSRlv5]')
print('bahamut_basecost_detail',bahamut_basecost_detail)
print('升技能总成本：',bahamut_basecost_detail_sum)
for x in range(1,15):
    print('lv',x,'->lv',x+1,'所需',bahamut_ssr_list[x],'成本',bahamut_basecost_detail[x],'合计',bahamut_basecost_detail_sum[x])
