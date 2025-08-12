
```
 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗                         
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗                        
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝                        
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗                        
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝                        
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝                         
                                                                      
██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗██╗   ██╗███████╗
██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔════╝
██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║█████╗  
██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║╚██╗ ██╔╝██╔══╝  
██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║ ╚████╔╝ ███████╗
╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
                                                                      
                                                                      
                                                                                             
```
# Github Detective: Bounty Hunter and Research Partner for Open Issues on Github

Locates high-impact issues on github using a combination of Github API; Python scripts and Dialogue with Claude Code CLI.

<img width="300" height="auto" alt="image" src="https://github.com/user-attachments/assets/c1959170-8f43-4638-84ac-d51020b049e0" />

## Workflow

```
.notes/ # 1. Design Prompts with Claude Code in .notes/
scripts/ # 2. Run the python scripts in scripts
data/ # 3. data will output here
.env # recommended: use API_GITHUB_TOKEN for more tool calls
```


## How to use

Fork this repo

empty .notes dir and data (they are examples of how to use)

Interact with Claude Code as your research partner to find issues


## process overview

1. User chooses Organisation(s) e.g. Shopify, Stripe, Playwright

2.  extract repositories, sort by PR velocity highest first with `30d_PR_merge_count`. Higher counts are a green flag.

3. select % of PR Velocity and filter out any repos (e.g. I don't want to work with Ruby on Rails)

4. extract open issues list, sort by recently opened

5. Define engagement criteria

6. Manually crawl through 50 most recent issues against engagement criteria (User deletes irrelevant files)