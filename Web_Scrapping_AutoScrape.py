
#(!pip install autoscraper) on terminal 
from autoscraper import AutoScraper



amazon_url ="https://www.amazon.com/s?k=Cap"

wanted_list = ["$27.99","Nike Golf - Dri-FIT Swoosh Perforated Cap , 429467, White, No Size","672"]

scraper=AutoScraper()
result= scraper.build(amazon_url,wanted_list)
print(result)

scraper.get_result_similar(amazon_url,grouped=True)

scraper.set_rule_aliases({'rule_jzvh':'Title','rule_b65c':'Price','rule_xqsd':'Rating'})
scraper.keep_rules(['rule_jzvh','rule_b65c','rule_xqsd'])
scraper.save('amazon-search')

results =scraper.get_result_similar('',group_by_alias= True)

results['Title']

