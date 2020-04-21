def create_permissions_file(list_of_emp_ids, number_of_levels):
    output_header=["CEO_" + str(i) if i!=0 else 'CEO' for i in range(number_of_levels)]
    output_header.insert(0,'Employee_id')
    f=open("./sample_permissions_file.csv", 'w')
    writer = csv.writer(f)
    writer.writerow(output_header)
    for i in list_of_emp_ids:
        writer.writerow([i]*(number_of_levels+2))
    f.close()