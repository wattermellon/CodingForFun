file_path1 = '2015-2016.txt'
file_path2 = '2017-2018.txt'
keyword = "Western Europe"

drug_approvals = {}
unique_drugs = set()


with open(file_path1, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        drug = parts[0]
        country = parts[1]
        approval = parts[2]
        income = parts[3]
        region = parts[4]

        # if region == keyword:
        unique_drugs.add(drug)
        if drug not in  drug_approvals:
                drug_approvals[drug] = []
        drug_approvals[drug].append(approval)

all_approval_drugs = [drug for drug, approvals in drug_approvals.items() if all(approval == 'Y' for approval in approvals)]

print(f"{len(all_approval_drugs)}")
print()
print(f"{len(unique_drugs)}")



drug_approvals = {}
unique_drugs = set()


with open(file_path2, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        drug = parts[0]
        country = parts[1]
        approval = parts[2]
        income = parts[3]
        region = parts[4]

        # if region == keyword:
        unique_drugs.add(drug)
        if  drug not in  drug_approvals:
                drug_approvals[drug] = []
        drug_approvals[drug].append(approval)

all_approval_drugs = [drug for  drug, approvals in drug_approvals.items() if all(approval == 'Y' for approval in approvals)]

print(f"{len(all_approval_drugs)}")
print()
print(f"{len(unique_drugs)}")
