def get_yomigana(text):
    node = mecab.parseToNode(text)
    yomi = ''
    while node:
        if node.surface:
            features = node.feature.split(',')
            if len(features) > 3 and features[3] != '*':
                yomi += features[3]
            else:
                yomi += node.surface
        node = node.next
    return yomi
