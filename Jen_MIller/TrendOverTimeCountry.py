file_path1 = '2015-2016.txt'
file_path2 = '2017-2018.txt'
keyword = "Western Europe"

country_approvals = {}
unique_countries = set()


with open(file_path1, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        drug = parts[0]
        country = parts[1]
        approval = parts[2]
        income = parts[3]
        region = parts[4]

        if region == keyword:
            unique_countries.add(country)
            if country not in country_approvals:
                country_approvals[country] = []
            country_approvals[country].append(approval)

all_approval_countries = [country for country, approvals in country_approvals.items() if all(approval == 'Y' for approval in approvals)]

print(f"Number of 1718 unique countries: {len(unique_countries)}")
print(f"Number of 1718 countries with all 'Y' approvals: {len(all_approval_countries)}")
# print("Countries with all 'Y' approvals:")
# for country in all_approval_countries:
#     print(country)


country_approvals = {}
unique_countries = set()


with open(file_path2, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        drug = parts[0]
        country = parts[1]
        approval = parts[2]
        income = parts[3]
        region = parts[4]

        if region == keyword:
            unique_countries.add(country)
            if country not in country_approvals:
                country_approvals[country] = []
            country_approvals[country].append(approval)

all_approval_countries = [country for country, approvals in country_approvals.items() if all(approval == 'Y' for approval in approvals)]

print(f"Number of 1718 unique countries: {len(unique_countries)}")
print(f"Number of 1718 countries with all 'Y' approvals: {len(all_approval_countries)}")