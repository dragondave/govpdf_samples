import requests
import lxml.html
import os

directory = "samples"
try:
    os.mkdir(directory)
except FileExistsError:
    pass



sources = {"nhs": "https://www.england.nhs.uk/commissioning/policies/ssp/",
           "psaa": "https://www.psaa.co.uk/appointing-auditors-and-fees/list-of-auditor-appointments-and-scale-fees/2021-22-auditor-appointments-and-fee-scale/consultation-on-2021-22-scale-fees/consultation-document-2021-22-audit-fee-scale-for-opted-in-local-government-and-police-bodies-january-2021/page/3/",
           "boundary": "https://boundarycommissionforengland.independent.gov.uk/data-and-resources/",
           "icai_a": "https://icai.independent.gov.uk/report/uk-aid-spending-during-covid-19-management-of-procurement-through-suppliers/",
           "icai_b": "https://icai.independent.gov.uk/report/the-uks-approach-to-tackling-modern-slavery-through-the-aid-programme/",
           "icai_c": "https://icai.independent.gov.uk/report/sexual-exploitation-and-abuse-by-international-peacekeepers/",
           "icai_d": "https://icai.independent.gov.uk/report/assessing-dfids-results-in-nutrition/",
           "icai_e": "https://icai.independent.gov.uk/report/uks-support-to-afdb-group/",
           "icai_f": "https://icai.independent.gov.uk/report/2018-19-follow-up/",
           "icai_g": "https://icai.independent.gov.uk/report/gavi-the-vaccine-alliance/",
           "icai_h": "https://icai.independent.gov.uk/report/uk-aid-spending-during-covid-19-management-of-procurement-through-suppliers/",
           "icai_i": "https://icai.independent.gov.uk/report/management-of-0-7-spending-target/",
           "icai_j": "https://icai.independent.gov.uk/report/the-uks-approach-to-tackling-modern-slavery-through-the-aid-programme/",
           "icai_k": "https://icai.independent.gov.uk/report/sexual-exploitation-and-abuse-by-international-peacekeepers/",
           "icai_l": "https://icai.independent.gov.uk/report/assessing-dfids-results-in-nutrition/",
           "icai_m": "https://icai.independent.gov.uk/report/uks-support-to-afdb-group/",
           "icai_n": "https://icai.independent.gov.uk/report/2018-19-follow-up/",
           "icai_o": "https://icai.independent.gov.uk/report/gavi-the-vaccine-alliance/",
           "icai_p": "https://icai.independent.gov.uk/report/anti-corruption/",
           "icai_q": "https://icai.independent.gov.uk/report/ghana/",
           "icai_r": "https://icai.independent.gov.uk/report/psvi/",
           "icai_s": "https://icai.independent.gov.uk/report/mutual-prosperity/",
           "icai_t": "https://icai.independent.gov.uk/report/management-of-0-7-spending-target/",}

seen_urls = set()

with open(f"{directory}/index.txt", "w") as index:
    for name, url in sources.items():
        r = requests.get(url)
        root = lxml.html.fromstring(r.content)
        pdf_tags = root.xpath("//a[contains(@href, '.pdf')]")
        for num, pdf_tag in enumerate(pdf_tags):
            shortname = f"{name}_{num}.pdf"
            pdf_url = pdf_tag.attrib['href']
            pdf_title = pdf_tag.text_content()
            if pdf_url in seen_urls:
                continue
            seen_urls.add(pdf_url)
            index.write(f'"{shortname}", "{pdf_url}", "{pdf_title}"\n')
            with open(f"{directory}/{shortname}", "wb") as pdf_file:
                pdf_file.write(requests.get(pdf_url).content)