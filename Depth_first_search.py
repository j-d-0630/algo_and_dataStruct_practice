def function(N,input_data):
    rslt = [[1,0,0]]
    [rslt.append([i+2,0,0]) for i in range(N-1)]
    count = 0
    stack_list = []
    #発見済リスト
    labeled_list = []
    #探索済リスト
    poped_list = []
    #(1)スタックSに最初のnodeを入れる
    s_node = input_data[0][0]
    stack_list.append(s_node)
    count += 1
    labeled_list.append(s_node)
    rslt[s_node-1][1] = count

    while(1):
        #(2)スタックSの1番上の要素を該当nodeとして参照する
        tgt_node = stack_list[len(stack_list)-1]
        #(3)該当nodeに隣接するnodeの内、若い番号のものをとってくる
        tmp = []
        for i in range(input_data[tgt_node-1][1]):
            tmp.append(input_data[tgt_node-1][2+i])
        

        if len(tmp) != 0:
            while(1):
                low_node = min(tmp)
                if (low_node in poped_list):
                    tmp.pop(tmp.index(low_node))
                    if len(tmp) == 0:
                        low_node = tgt_node
                        break
                else:
                    break
                
        else:
            low_node = tgt_node
        
        #未探索nodeなら探索中のラベルをつけてスタックSにプッシュして(2)に戻る
        if (low_node not in labeled_list):
            count += 1
            labeled_list.append(low_node)
            rslt[low_node-1][1] = count
            stack_list.append(low_node)
        #未探索nodeじゃなかったらスタックSからポップして探索済のラベルをつける
        elif (low_node in stack_list):
            count += 1
            poped_list.append(low_node)
            rslt[low_node-1][2] = count
            stack_list.pop(stack_list.index(low_node))
        
        #(4)スタックSが空でないなら(2)に戻る
        if len(poped_list) == len(input_data):
            break
    
    return rslt


N = int(input())
input_data = [list(map(int,input().split())) for i in range(N)]
ans = function(N,input_data)

print("出力：")

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if j != len(ans[i])-1:
            print(ans[i][j],"",end='')
        else:
            print(ans[i][j])