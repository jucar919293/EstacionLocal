import datetime
def create_file(file_name,lines,ext):
    file_name = file_name + ext
    with open(file_name,'w') as f:
        for i in range(lines):
            f.write("This is line {} \n".format(i))


def create_images(estation,n_images,path):

    now = datetime.datetime.now()
    repeat = 0

    for i in range(n_images):
        if i> 60:
            i = 59
        minute = i
        second = i

        repeat = repeat+1
        if repeat>9:
            repeat = 0

        created = datetime.datetime(now.year, now.month, 
                                    now.day, 23,
                                    minute, second)
        
        day_format = created.strftime('%Y%d%m')
        time_format = created.strftime('%H%M%S')
        name = '{}_X_{}_{}_00{}'.format(estation,day_format,time_format,repeat)

        create_file(path+name,5,'.img')