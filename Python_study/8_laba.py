
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
class Contract:
    def __init__(self, computer_type, supplier, cpu):
        self.computer_type = computer_type
        self.supplier = supplier
        self.cpu= cpu
    def get_computer_type(self):
        return self.computer_type
    def get_supplier(self):
        return self.supplier
    def get_cpu(self):
        return self.cpu
def load_data(t,file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            contracts = []
            for row in reader:
                computer_type, supplier, cpu = row
                try: cpu = int(cpu)
                except ValueError: 
                    contracts=[]
                    t.delete(1.0,tk.END)
                    t.insert(1.0,f"Некорректный ввод мощности процессора в строчке {reader.line_num}")
                    break
                else:
                    t.insert(tk.END,f'{computer_type} {supplier} {cpu}\n')
                    contract = Contract(computer_type, supplier, cpu)
                    contracts.append(contract)
        return contracts
    except FileNotFoundError:
        print("File not found.")
        return []
def segment_by_computer_type(contracts):
    segmentation = {}
    for contract in contracts:
        computer_type = contract.get_computer_type()
        if computer_type not in segmentation:
            segmentation[computer_type] = []
        segmentation[computer_type].append(contract)
    return segmentation
def visualize_computer_type_pie_chart(window, segmentation):
    canvas = tk.Canvas(window, width=550, height=550)
    canvas.grid(row=1, column=1)
    labels = list(segmentation.keys())
    sizes = [len(contracts) for contracts in segmentation.values()]
    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Сегментация договоров по типам")
    canvas_agg = FigureCanvasTkAgg(fig, canvas)
    canvas_agg.draw()
    canvas_agg.get_tk_widget().pack()
def segment_by_supplier(contracts):
    segmentation = {}
    for contract in contracts:
        supplier = contract.get_supplier()
        if supplier not in segmentation:
            segmentation[supplier] = []
        segmentation[supplier].append(contract)
    return segmentation
def visualize_supplier_pie_chart(window,segmentation):
    canvas = tk.Canvas(window, width=550, height=550)
    canvas.grid(row=1, column=0)
    labels = list(segmentation.keys())
    sizes = [len(contracts) for contracts in segmentation.values()]
    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Сегментация договоров по поставщикам")
    canvas_agg = FigureCanvasTkAgg(fig, canvas)
    canvas_agg.draw()
    canvas_agg.get_tk_widget().pack()
def main():
    window = tk.Tk()
    window.title("Программа отображения сегментаций списка договоров")
    window.geometry("1000x700")
    window.columnconfigure(index=0, weight=700)
    window.columnconfigure(index=1, weight=700)
    lbl1=tk.Label(font='9', text="Сегментация договоров по типам компьютеров")
    lbl2=tk.Label(font='9', text="Сегментация договоров по поставщикам компьютеров")
    lbl3=tk.Label(font='9', text="Тип | Поставщик | Мощность процессора")
    t = tk.Text(window,height=7,font='9', width = 700)
    t.grid(row=3,column=0, columnspan=2, sticky='ew',pady=10)
    scrollbar = tk.Scrollbar(orient="vertical", command = t.yview)
    t["yscrollcommand"]=scrollbar.set
    scrollbar.grid(row=3,column=0,columnspan=2,sticky='nse')
    t.yview_scroll(number=1, what="units")
    scrollbar.config(command=t.yview)
    btn1 = tk.Button(font='9',text='Завершить программу', command= lambda: window.quit())
    contracts = load_data(t,'8.csv')
    if contracts:
        lbl1.grid(row=0, column=0, padx=10, pady=10)
        lbl2.grid(row=0, column=1, padx=10, pady=10)
        lbl3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        segmentation = segment_by_computer_type(contracts)
        visualize_computer_type_pie_chart(window,segmentation)
        segmentation = segment_by_supplier(contracts)
        visualize_supplier_pie_chart(window,segmentation)
    btn1.grid(row=4, column=0, columnspan=2,pady=20)
    window.mainloop()
main()