# coding:utf-8
import os
import router
import json
def MinerInfo(action):
    out = os.popen('docker exec miner miner '+action)
    info = out.read()
    #lines=info.split('\n')#通过换行进行分割
    return info;

def print_keys():
    raw = MinerInfo("print_keys");
    lines=raw.split('\n')
    ret = []
    if(len(lines)>1):
        for it in lines:
           row = it.split('.')
           ret.append(row[0])
        return json.dumps(ret)
    else :
        return router.server_error();

def info_height():
    try:
        raw = MinerInfo("info height");
        row = raw.split('\n')[0]
        BlockAge = row.split("\t\t")[0];
        SyncHeight = row.split("\t\t")[1];
        return json.dumps({'BlockAge':BlockAge,'SyncHeight':SyncHeight});
    except:
        return router.server_error();


if __name__ == '__main__':
    print(info_height())
