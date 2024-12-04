print('Hoàng Thanh Kiếm MSSV 235752021610003')
def tim_tu_dai_nhat(van_ban):
    tu_list = van_ban.split()
    max_length = max(len(tu) for tu in tu_list)
    tu_dai_nhat = [tu for tu in tu_list if len(tu) == max_length]
    return tu_dai_nhat
van_ban = "Đào Quang Huy"
tu_dai_nhat = tim_tu_dai_nhat(van_ban)
print("Những từ dài nhất trong văn bản là:")
for tu in tu_dai_nhat:
    print(tu)
