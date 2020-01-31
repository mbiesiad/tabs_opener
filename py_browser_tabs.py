import webbrowser
list_sites = []
blog = 'https://c0dingp0int3r.design.blog'
gitlab = 'https://gitlab.com/biesiad'
github = 'https://github.com/mbiesiad'
list_sites.append(blog)
list_sites.append(gitlab)
list_sites.append(github)

for tab in range(0, 3):
    webbrowser.open(list_sites[tab], new=2)
