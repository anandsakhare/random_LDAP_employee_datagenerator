def create_permissions_file(list_of_emp_ids, number_of_levels):
    output_header=["ceo_" + str(i) if i!=0 else 'ceo' for i in range(number_of_levels)]
    output_header.insert(0,'UserName')
    f=open("./sample_permissions_file.csv", 'w')
    writer = csv.writer(f)
    writer.writerow(output_header)
    for i in list_of_emp_ids:
        for j in range(1,len(output_header)):
            l = [None] * (len(output_header))
            l[j]=i
            l[0]=i
            print(l)
            writer.writerow(l)
    f.close()