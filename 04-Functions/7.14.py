def n_operation(n1,n2,operation):
    return {'+':n1+n2,'%':n1%n2,'**':n1**n2,'*':n1*n2,'-':n1-n2}[operation]
for oper in ['+','%','**','*',"-"]:
    print(n_operation(2,3,oper))