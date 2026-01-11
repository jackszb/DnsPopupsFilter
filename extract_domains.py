import requests
import re

# GitHub 上的文件 URL
url = 'https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/filters/general/filter_59_DnsPopupsFilter/filter.txt'

# 发送 GET 请求下载文件
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 获取文件内容
    content = response.text

    # 移除空行
    content = '\n'.join([line for line in content.split('\n') if line.strip() != ''])

    # 使用正则表达式提取域名
    domain_pattern = re.compile(r'^(?:https?://)?([a-zA-Z0-9.-]+)')
    domains = set(re.findall(domain_pattern, content))

    # 保存到文件
    with open('domain_list.txt', 'w') as f:
        for domain in sorted(domains):
            f.write(domain + '\n')

    print("域名提取完成，保存在 domain_list.txt 文件中。")
else:
    print(f"下载文件失败，HTTP 状态码：{response.status_code}")
