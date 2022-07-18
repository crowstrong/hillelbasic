file_name: str = 'data.txt'
data: dict = {'usd_rate': 27.5, 'usd_total': 13500.98, 'uah_rate': 27.3, 'uah_total': 39345.5}


def save_to_file() -> None:
    f = open(file_name, 'w')
    s1 = str(data['usd_rate']) + '\n'
    s2 = str(data['usd_total']) + '\n'
    s3 = str(data['uah_rate']) + '\n'
    s4 = str(data['uah_total']) + '\n'
    f.writelines([s1, s2, s3, s4])


def load_from_file() -> None:
    try:
        f = open(file_name, 'r')
        s1 = f.readline()
        data['usd_rate'] = float(s1)
        s2 = f.readline()
        data['usd_total'] = float(s2)
        s3 = f.readline()
        data['uah_rate'] = float(s3)
        s4 = f.readline()
        data['uah_total'] = float(s4)
    except Exception as e:
        print('Does not contain required values in data.txt', e)
        exit()


if __name__ == '__main__':
    save_to_file()  # create a file called data.txt with currency data
    load_from_file()  # call foo from taking a data from data.txt
    while True:
        menu: str = input('COMMAND?\n').upper()
        params: list = menu.split()
        if params[0] == 'COURSE':
            if params[1] == 'USD':
                print('RATE ', data['usd_rate'], ', AVAILABLE ', round(data['usd_total'], 2), sep='')
            elif params[1] == 'UAH':
                print('RATE ', data['uah_rate'], ', AVAILABLE ', round(data['uah_total'], 2), sep='')
            else:
                print('INVALID CURRENCY', params[1])
        elif params[0] == 'EXCHANGE':
            if params[1] == 'USD':
                if float(params[2]) * data['uah_rate'] <= data['uah_total']:
                    data['usd_total'] += float(params[2])
                    data['uah_total'] -= float(params[2]) * data['uah_rate']
                    save_to_file()  # call foo for saving a new UAH currency data
                    print('UAH ', float(params[2]) * data['uah_rate'], ', RATE ', data['uah_rate'], sep='')
                else:
                    print('UNAVAILABLE, REQUIRED BALANCE UAH ', float(params[2]) * data['uah_rate'],
                          ', AVAILABLE ', data['uah_total'], sep='')
            elif params[1] == 'UAH':
                if float(params[2]) / data['usd_rate'] <= data['usd_total']:
                    data['uah_total'] += float(params[2])
                    data['usd_total'] -= float(params[2]) / data['usd_rate']
                    save_to_file()  # call foo for saving a new USD currency data
                    print('USD ', round(float(params[2]) / data['usd_rate'], 2), ', RATE ',
                          round(1 / data['usd_rate'], 3), sep='')
                else:
                    print('UNAVAILABLE, REQUIRED BALANCE USD ', round(float(params[2]) / data['usd_rate'], 2),
                          ', AVAILABLE ', data['usd_total'], sep='')
            else:
                print('INVALID CURRENCY', params[1])
        elif params[0] == 'STOP':
            print('SERVICE STOPPED')
            exit()
