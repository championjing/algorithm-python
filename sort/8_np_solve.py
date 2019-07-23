#coding=utf-8
# 要覆盖的州,使用集合表示，因为在集合中同样的元素不能重复，可进行并集、交集、差集操作
states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])
# 使用散列表表示广播清单
stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])
# 用来存储最终选择的广播台
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # 两个集合的与操作，得到两个集合的交集
        covered = states_needed & states_for_station
        if len( covered ) > len( states_covered ):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add( best_station )

print( final_stations )