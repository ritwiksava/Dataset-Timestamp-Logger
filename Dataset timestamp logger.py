import time 

def get_data():
    data = input("Enter sensors data value ( q for quit):")
    return data

def log_data(data):
    timestamp = time.strftime("%Y:%m:%d : %H:%M:%S")

    with open(r"C:\Users\Ritwik\OneDrive\Desktop\pythonpink\bro code\dataset.txt" , 'a') as file:
        file.write(f"{timestamp} : {data} \n")
    print("Data logged sucessfully")
    
def main():
    while True :
        data = get_data()

        if data.lower() == "q":
            print("Logging stopped")
            break 

        data = float(data)
        log_data(data)
          
main()