from .dictionary import (
    TOKENS,
    PARTERNS,
    UNKOWN_TOKEN,
    RELATIONS,
    DB_PATH,
    MAP_RELATION_TO_DB,
)
import re
from functools import reduce


def convertDict1(key, values):
    return [[i[0], i[1], key] for i in values]


def convertDict2(key, values):
    return [[i, key] for i in values]


def parsePartern(input):
    parterns = [convertDict1(k, PARTERNS[k]) for k in PARTERNS]
    parterns = reduce(lambda x, y: x+y, parterns, [])
    keyParterns = [p[0] for p in parterns]
    s = input.lower().strip()
    mapTokens = []
    while(len(s)):
        unReconigze = True
        for i in TOKENS:
            match = re.match(i[0], s)
            if bool(match):
                mapTokens.append((match.group(0), i[1]))
                unReconigze = False
                break
        if unReconigze:
            mapTokens.append((s.split()[0], UNKOWN_TOKEN))
        s = s[len(mapTokens[-1][0]):].strip()
    return handleMapTokens(mapTokens, parterns, keyParterns)


def handleMapTokens(mapTokens, parterns, keyParterns):
    result = []
    while len(mapTokens):
        listCheck = list(range(1, len(mapTokens)+1))
        listCheck.reverse()
        isNotExist = True
        for i in listCheck:
            typeTokens = [t[1] for t in mapTokens[:i]]
            if typeTokens in keyParterns:
                index = keyParterns.index(typeTokens)
                w = mapTokens[:i][parterns[index][1]][0]
                for i in range(i):
                    mapTokens.pop(0)
                mapTokens.insert(0, (w, parterns[index][2]))
                isNotExist = False
                continue
        if isNotExist:
            result.append(mapTokens.pop(0))
    if result[0][1] in ['w_tra', 'w_t'] and result[-1][1] == 'w':
        result = result[:-1]
    return result


def handelLogicalForm(parterns):
    relations = [convertDict2(k, RELATIONS[k]) for k in RELATIONS]
    relations = reduce(lambda x, y: x+y, relations, [])
    parternType = [i[1] for i in parterns]
    result = []
    for r in relations:
        rValid = True
        listItem = []
        listIndex = []
        for item in r[0]:
            if item in parternType:
                index = parternType.index(item)
                if index in listIndex:
                    rValid = False
                    continue
                listIndex.append(index)
                listItem.append(parterns[index][0])
            else:
                rValid = False
        if rValid:
            result.append([r[1], r[0], listItem])
    return result


def handleQueryForm(logicalForm):
    result = []
    for l in logicalForm:
        mapped = MAP_RELATION_TO_DB[l[0]]
        for i, m in enumerate(mapped):
            for j, v in enumerate(m):
                if v[0] == '*':
                    if v[-1] == 'l':
                        mapped[i][j] = convertLocation(l[2][int(v[1:-1])])
                    elif v[-1] == 't':
                        mapped[i][j] = convertTime(l[2][int(v[1:-1])])
                    elif v[-1] == 'b':
                        mapped[i][j] = l[2][int(v[1:-1])].upper()
        result += mapped
    return mergeQueryFromRaw(result)


def mergeQueryFromRaw(query):
    dictQ = {}
    for i in query:
        if i[0] not in dictQ:
            dictQ[i[0]] = []
        dictQ[i[0]].append(i)
    for key in dictQ:
        values = dictQ[key]
        if len(values) > 1:
            zipV = zip(*values)
            result = []
            for i in zipV:
                result.append(priority(i))
            dictQ[key] = [result]
    return [dictQ[i][0] for i in dictQ]


def priority(t):
    for i in t:
        if i[0] != '?':
            return i
    return t[0]


def searchInDb(query):
    findInfo = query[0][1]
    if findInfo == '?t':
        id = ''
        for i in query:
            if i[0] == 'BUS':
                id = i[1]
                break
        q_t = [q for q in query if q[0] in ['RUN-TIME']]
        if len(q_t) and '?l' not in q_t[0]:
            query = [q for q in query if q[0] not in ['ATIME', 'DTIME']]
        elif len(q_t):
            query = [q for q in query if q[0] not in ['RUN-TIME']]
        for i, q in enumerate(query):
            for j, v in enumerate(q):
                if v == '?b':
                    query[i][j] = id
    query = query[1:]
    query = [q for q in query if findInfo in q]
    db = loadDb()
    result = []
    for q in query:
        candidate = set()
        for d in db:
            if len(q) == len(d):
                isMatch = True
                for i, j in zip(q, d):
                    if i[0] != '?' and i != j:
                        isMatch = False
                        break
                if isMatch:
                    for i, j in zip(q, d):
                        if i == findInfo:
                            candidate.add(j)
        result.append(candidate)
    return reduce(lambda a, b: a.intersection(b), result)


def formatDependences(dependences):
    result = []
    for i in dependences:
        result.append('('+i[0] + ' ' + i[1][-1] + '{' + i[2][-1]+'})')
    result = '\n'.join(result)
    return result


def convertLocation(location):
    if location == 'huế':
        return 'HUE'
    elif location == "hồ chí minh":
        return "HCMC"
    elif location == 'đà nẵng':
        return 'DANANG'


def convertTime(t):
    return t+'HR'


def loadDb():
    result = []
    with open(DB_PATH) as db:
        for line in db:
            result.append(line.strip()[1:-1].split())
    return result
