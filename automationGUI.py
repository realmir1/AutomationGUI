from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

class Hospital:
    def __init__(self, root):
        self.client = None
        self.db = None
        self.collection = None
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client["HospitalDB"]
            self.collection = self.db["Patients"]
            print("MongoDB'ye başarıyla bağlandı!")
        except Exception as e:
            messagebox.showerror("MongoDB Bağlantı Hatası",
                                 f"MongoDB'ye bağlanılamadı: {e}\n"
                                 "Lütfen MongoDB sunucusunun çalıştığından emin olun ve bağlantı adresini kontrol edin.")

        self.root = root
        self.root.title("Hastane Yönetim Sistemi")
        self.root.geometry("1540x800+0+0")
        self.root.config(bg="grey")

        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientID = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()


        lbltitle = Label(self.root, bd=12, relief=RIDGE, text="HASTANE YÖNETİM SİSTEMİ",
                         fg="white", bg="grey", font=("sans-herif", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)


        Dataframe = Frame(self.root, bd=0, relief=RIDGE)
        Dataframe.place(x=0, y=135, width=1530, height=500)


        DataframeLeft = LabelFrame(Dataframe, bd=1, relief=RIDGE, padx=20,
                                   font=("sans_herif", 10, "normal"), text="Hasta Bilgileri")
        DataframeLeft.place(x=20, y=10, width=820, height=350)


        DataframeRight = LabelFrame(Dataframe, bd=1, relief=RIDGE, padx=20,
                                    font=("sans-herif", 10, "normal"), text="Reçete")
        DataframeRight.place(x=900, y=5, width=600, height=350)


        Buttonframe = Frame(self.root, bd=1, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=60)


        Detailsframe = Frame(self.root, bd=1, relief=RIDGE)
        Detailsframe.place(x=0, y=624, width=1530, height=600)



        lblNameTable = Label(DataframeLeft, text="Tablet Adı", font=("ariel", 12, "bold"), padx=2, pady=6)
        lblNameTable.grid(row=0, column=0, sticky=W)
        comNametablet = ttk.Combobox(DataframeLeft, font=("times new roman", 15, "bold"),
                                    width=33, textvariable=self.NameofTablets)
        comNametablet["values"] = (
    # 1–50: Ağrı Kesiciler ve NSAİİ
    "Paracetamol", "Ibuprofen", "Aspirin", "Naproxen", "Diclofenac", "Meloxicam", "Celecoxib", "Ketoprofen", "Piroxicam", "Indomethacin",
    "Etodolac", "Dexketoprofen", "Nimesulide", "Metamizole", "Flurbiprofen", "Tiaprofenoic Acid", "Aceclofenac", "Mephenamic Acid", "Tolfenamic Acid", "Oxaprozin",
    "Lornoxicam", "Sulindac", "Tenoxicam", "Nabumetone", "Phenylbutazone", "Ketorolac", "Choline Magnesium Trisalicylate", "Salicylamide", "Diflunisal", "Tolmetin",
    "Zaltoprofen", "Tapentadol", "Tramadol", "Codeine", "Hydrocodone", "Oxycodone", "Morphine", "Buprenorphine", "Nalbuphine", "Pethidine",
    "Methadone", "Fentanyl", "Lidocaine", "Gabapentin", "Pregabalin", "Carbamazepine", "Lamotrigine", "Valproic Acid", "Levetiracetam", "Topiramate",

    # 51–100: Antibiyotik ve Antiviral
    "Amoxicillin", "Amoxicillin+Clavulanate", "Cefuroxime", "Cefixime", "Cephalexin", "Cefdinir", "Cefpodoxime", "Ceftriaxone", "Penicillin V", "Penicillin G",
    "Doxycycline", "Tetracycline", "Minocycline", "Azithromycin", "Erythromycin", "Clarithromycin", "Clindamycin", "Metronidazole", "Tinidazole", "Nitrofurantoin",
    "Ciprofloxacin", "Levofloxacin", "Moxifloxacin", "Ofloxacin", "Rifampin", "Linezolid", "Vancomycin", "Imipenem", "Meropenem", "Sulfamethoxazole+Trimethoprim",
    "Oseltamivir", "Acyclovir", "Valacyclovir", "Famciclovir", "Lamivudine", "Tenofovir", "Efavirenz", "Nevirapine", "Rilpivirine", "Abacavir",
    "Ribavirin", "Sofosbuvir", "Remdesivir", "Zidovudine", "Didanosine", "Raltegravir", "Lopinavir", "Darunavir", "Atazanavir", "Dolutegravir",

    # 101–150: Kalp, Tansiyon, Kolesterol
    "Amlodipine", "Lisinopril", "Enalapril", "Ramipril", "Perindopril", "Captopril", "Losartan", "Valsartan", "Irbesartan", "Telmisartan",
    "Olmesartan", "Hydrochlorothiazide", "Chlorthalidone", "Indapamide", "Furosemide", "Spironolactone", "Eplerenone", "Metoprolol", "Atenolol", "Bisoprolol",
    "Nebivolol", "Carvedilol", "Propranolol", "Diltiazem", "Verapamil", "Nifedipine", "Clonidine", "Methyldopa", "Minoxidil", "Digoxin",
    "Atorvastatin", "Rosuvastatin", "Simvastatin", "Pravastatin", "Fluvastatin", "Pitavastatin", "Ezetimibe", "Fenofibrate", "Gemfibrozil", "Niacin",

    # 151–200: Mide / Sindirim
    "Omeprazole", "Pantoprazole", "Esomeprazole", "Rabeprazole", "Lansoprazole", "Ranitidine", "Famotidine", "Domperidone", "Itopride", "Metoclopramide",
    "Magaldrate", "Aluminium Hydroxide", "Calcium Carbonate", "Simethicone", "Sucralfate", "Misoprostol", "Mesalamine", "Sulfasalazine", "Loperamide", "Bisacodyl",
    "Senna", "Docusate", "Lactulose", "Psyllium", "Polyethylene Glycol", "Dulcolax", "Pancreatin", "Digestive Enzyme", "Ondansetron", "Granisetron",
    "Aprepitant", "Meclizine", "Hyoscine", "Dicyclomine", "Butylscopolamine", "Bismuth Subsalicylate", "Rifaximin", "Ursodeoxycholic Acid", "Cholestyramine", "Budesonide",

    # 201–250: Psikiyatri ve Nöroloji
    "Fluoxetine", "Sertraline", "Paroxetine", "Citalopram", "Escitalopram", "Venlafaxine", "Duloxetine", "Amitriptyline", "Nortriptyline", "Imipramine",
    "Trazodone", "Mirtazapine", "Bupropion", "Vortioxetine", "Lithium", "Risperidone", "Olanzapine", "Quetiapine", "Aripiprazole", "Ziprasidone",
    "Haloperidol", "Chlorpromazine", "Perphenazine", "Clozapine", "Lurasidone", "Diazepam", "Alprazolam", "Lorazepam", "Clonazepam", "Midazolam",
    "Zolpidem", "Zopiclone", "Melatonin", "Buspirone", "Modafinil", "Methylphenidate", "Atomoxetine", "Adderall", "Ritalin", "Donepezil",

    # 251–300: Hormonlar, Vit., Kadın Sağlığı, Diğer
    "Levothyroxine", "Liothyronine", "Methimazole", "Propylthiouracil", "Prednisolone", "Dexamethasone", "Hydrocortisone", "Betamethasone", "Fludrocortisone", "Estrogen",
    "Progesterone", "Ethinylestradiol", "Levonorgestrel", "Drospirenone", "Desogestrel", "Norethisterone", "Letrozole", "Tamoxifen", "Raloxifene", "Clomiphene",
    "Vitamin D", "Vitamin B12", "Vitamin B6", "Vitamin C", "Folic Acid", "Iron Tablet", "Zinc", "Magnesium", "Calcium", "Multivitamin",
    "Biotin", "Coenzyme Q10", "Glucosamine", "Chondroitin", "Isotretinoin", "Finasteride", "Tamsulosin", "Sildenafil", "Vardenafil", "Alendronate"


)

        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        l1bref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Referans No:", padx=2)
        l1bref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ref)
        txtref.grid(row=1, column=1)

        l1bDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Doz:", padx=2, pady=4)
        l1bDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        l1bNooftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="Tablet Sayısı:", padx=2, pady=6)
        l1bNooftablets.grid(row=3, column=0, sticky=W)
        txtNooftablets = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.NumberofTablets)
        txtNooftablets.grid(row=3, column=1)

        l1bLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        l1bLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        l1bIssueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Veriliş Tarihi:", padx=2, pady=6)
        l1bIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Issuedate)
        txtIssueDate.grid(row=5, column=1)

        l1bExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Son Kullanma Tarihi:", padx=2, pady=6)
        l1bExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ExpDate)
        txtExpDate.grid(row=6, column=1)

        l1bDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Günlük Doz:", padx=2, pady=4)
        l1bDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.DailyDose)
        txtDailyDose.grid(row=7, column=1)

        l1bSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Yan Etki:", padx=2, pady=6)
        l1bSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.sideEffect)
        txtSideEffect.grid(row=8, column=1)

        l1bFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Ek Bilgi", padx=2)
        l1bFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.furtherInformation)
        txtFurtherinfo.grid(row=0, column=3)

        l1bBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="Kan Basıncı", padx=2, pady=6)
        l1bBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DrivingUsingMachine)
        txtBloodPressure.grid(row=1, column=3)

        l1bStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Saklama Tavsiyesi:", padx=2, pady=6)
        l1bStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.StorageAdvice)
        txtStorage.grid(row=2, column=3)

        l1bMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="İlaç Kullanımı", padx=2, pady=6)
        l1bMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.HowToUseMedication)
        txtMedicine.grid(row=3, column=3, sticky=W)

        l1bPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Hasta Kimliği", padx=2, pady=6)
        l1bPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientID)
        txtPatientId.grid(row=4, column=3)

        l1bNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Numarası", padx=2, pady=6)
        l1bNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.nhsNumber)
        txtNhsNumber.grid(row=5, column=3)

        l1bPatientname = Label(DataframeLeft, font=("arial", 12, "bold"), text="Hasta Adı", padx=2, pady=6)
        l1bPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientName)
        txtPatientname.grid(row=6, column=3)

        l1bDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Doğum Tarihi", padx=2, pady=6)
        l1bDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DateOfBirth)
        txtDateOfBirth.grid(row=7, column=3)

        l1bPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Hasta Adresi", padx=2, pady=6)
        l1bPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=8, column=3)


        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "normal"), width=78, height=22, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        btnPresciription = Button(Buttonframe, text="Reçete Oluştur", bg="white", fg="black",
                                  font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                                  command=self.iPrescription)
        btnPresciription.grid(row=0, column=0)

        btnPresciriptionData = Button(Buttonframe, text="Veri Kaydet", bg="green", fg="black",
                                      font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                                      command=self.iPrescriptionData)
        btnPresciriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Güncelle", bg="green", fg="black",
                           font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                           command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Sil", bg="green", fg="black",
                           font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                           command=self.idelete)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Temizle", bg="green", fg="black",
                          font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                          command=self.iClear)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Çıkış", bg="green", fg="black",
                         font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6,
                         command=self.iExit)
        btnExit.grid(row=0, column=5)

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)


        self.hospital_table = ttk.Treeview(Detailsframe, columns=(
            "nameoftablet", "ref", "dose", "nooftablets", "lot", "issuedate",
            "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address",
            "sideEffect", "furtherInformation", "bloodPressure", "medication", "patientID"
        ),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet", text="Tablet Adı")
        self.hospital_table.heading("ref", text="Referans No.")
        self.hospital_table.heading("dose", text="Doz")
        self.hospital_table.heading("nooftablets", text="Tablet Sayısı")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Veriliş Tarihi")
        self.hospital_table.heading("expdate", text="Son Kullanma Tarihi")
        self.hospital_table.heading("dailydose", text="Günlük Doz")
        self.hospital_table.heading("storage", text="Saklama Tavsiyesi")
        self.hospital_table.heading("nhsnumber", text="NHS Numarası")
        self.hospital_table.heading("pname", text="Hasta Adı")
        self.hospital_table.heading("dob", text="Doğum Tarihi")
        self.hospital_table.heading("address", text="Adres")
        self.hospital_table.heading("sideEffect", text="Yan Etki")
        self.hospital_table.heading("furtherInformation", text="Ek Bilgi")
        self.hospital_table.heading("bloodPressure", text="Kan Basıncı")
        self.hospital_table.heading("medication", text="İlaç Kullanımı")
        self.hospital_table.heading("patientID", text="Hasta Kimliği")
        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=80)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=80)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=120)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=120)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=150)
        self.hospital_table.column("sideEffect", width=100)
        self.hospital_table.column("furtherInformation", width=120)
        self.hospital_table.column("bloodPressure", width=100)
        self.hospital_table.column("medication", width=100)
        self.hospital_table.column("patientID", width=100)


        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)


        if self.collection is not None:
            self.fetch_data()


    def iPrescription(self):

        if (self.NameofTablets.get() == "" or self.ref.get() == "" or self.PatientID.get() == "" or
                self.PatientName.get() == ""):
            messagebox.showerror("Hata", "Tüm zorunlu alanlar doldurulmalıdır (Tablet Adı, Referans No, Hasta Kimliği, Hasta Adı).")
            return

        self.txtPrescription.delete("1.0", END)
        self.txtPrescription.insert(END, "Hastane Yönetim Sistemi\n")
        self.txtPrescription.insert(END, "-------------------------------------\n")
        self.txtPrescription.insert(END, f"Tablet Adı:\t\t\t{self.NameofTablets.get()}\n")
        self.txtPrescription.insert(END, f"Referans No:\t\t\t{self.ref.get()}\n")
        self.txtPrescription.insert(END, f"Doz:\t\t\t\t{self.Dose.get()}\n")
        self.txtPrescription.insert(END, f"Tablet Sayısı:\t\t\t{self.NumberofTablets.get()}\n")
        self.txtPrescription.insert(END, f"Lot No:\t\t\t\t{self.Lot.get()}\n")
        self.txtPrescription.insert(END, f"Veriliş Tarihi:\t\t\t{self.Issuedate.get()}\n")
        self.txtPrescription.insert(END, f"Son Kullanma Tarihi:\t\t{self.ExpDate.get()}\n")
        self.txtPrescription.insert(END, f"Günlük Doz:\t\t\t{self.DailyDose.get()}\n")
        self.txtPrescription.insert(END, f"Yan Etki:\t\t\t{self.sideEffect.get()}\n")
        self.txtPrescription.insert(END, f"Ek Bilgi:\t\t\t{self.furtherInformation.get()}\n")
        self.txtPrescription.insert(END, f"Saklama Tavsiyesi:\t\t{self.StorageAdvice.get()}\n")
        self.txtPrescription.insert(END, f"Kan Basıncı/Makine Kullanımı:\t{self.DrivingUsingMachine.get()}\n")
        self.txtPrescription.insert(END, f"İlaç Kullanım Bilgisi:\t\t{self.HowToUseMedication.get()}\n")
        self.txtPrescription.insert(END, f"Hasta Kimliği:\t\t\t{self.PatientID.get()}\n")
        self.txtPrescription.insert(END, f"NHS Numarası:\t\t\t{self.nhsNumber.get()}\n")
        self.txtPrescription.insert(END, f"Hasta Adı:\t\t\t{self.PatientName.get()}\n")
        self.txtPrescription.insert(END, f"Doğum Tarihi:\t\t\t{self.DateOfBirth.get()}\n")
        self.txtPrescription.insert(END, f"Hasta Adresi:\t\t\t{self.PatientAddress.get()}\n")
        self.txtPrescription.insert(END, "-------------------------------------\n")
        self.txtPrescription.insert(END, f"Tarih: {time.asctime(time.localtime(time.time()))}\n")

    def iPrescriptionData(self):
        if self.collection is None:
            messagebox.showerror("Hata", "MongoDB bağlantısı kurulamadı. Veri kaydedilemiyor.")
            return

        if (self.NameofTablets.get() == "" or self.PatientID.get() == "" or
                self.PatientName.get() == ""):
            messagebox.showerror("Hata", "Tablet Adı, Hasta Kimliği ve Hasta Adı boş bırakılamaz.")
            return

        if self.ref.get() == "":
            rand_ref = str(random.randint(10000, 99999))
            self.ref.set(rand_ref)

        patient_data = {
            "nameoftablet": self.NameofTablets.get(),
            "ref": self.ref.get(),
            "dose": self.Dose.get(),
            "nooftablets": self.NumberofTablets.get(),
            "lot": self.Lot.get(),
            "issuedate": self.Issuedate.get(),
            "expdate": self.ExpDate.get(),
            "dailydose": self.DailyDose.get(),
            "sideEffect": self.sideEffect.get(),
            "furtherInformation": self.furtherInformation.get(),
            "storage": self.StorageAdvice.get(),
            "drivingUsingMachine": self.DrivingUsingMachine.get(),
            "howToUseMedication": self.HowToUseMedication.get(),
            "patientID": self.PatientID.get(),
            "nhsnumber": self.nhsNumber.get(),
            "pname": self.PatientName.get(),
            "dob": self.DateOfBirth.get(),
            "address": self.PatientAddress.get()
        }

        try:
            self.collection.insert_one(patient_data)
            messagebox.showinfo("Başarılı", "Hasta reçete verisi başarıyla MongoDB'ye eklendi.")
            self.fetch_data()
            self.iClear()
        except Exception as e:
            messagebox.showerror("Hata", f"Veri kaydedilirken bir hata oluştu: {e}")

    def get_cursor(self, event=""):

        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        if row:


            self.NameofTablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])
            self.sideEffect.set(row[13])
            self.furtherInformation.set(row[14])
            self.DrivingUsingMachine.set(row[15])
            self.HowToUseMedication.set(row[16])
            self.PatientID.set(row[17])

            self.iPrescription()

    def update_data(self):
        if self.collection is None:
            messagebox.showerror("Hata", "MongoDB bağlantısı kurulamadı. Veri güncellenemiyor.")
            return

        selected_item = self.hospital_table.focus()
        if not selected_item:
            messagebox.showerror("Hata", "Güncellenecek bir kayıt seçin.")
            return

        confirm = messagebox.askyesno("Güncelleme Onayı", "Seçilen kaydı güncellemek istediğinizden emin misiniz?")
        if confirm:
            current_ref = self.ref.get()
            updated_data = {
                "nameoftablet": self.NameofTablets.get(),
                "ref": self.ref.get(),
                "dose": self.Dose.get(),
                "nooftablets": self.NumberofTablets.get(),
                "lot": self.Lot.get(),
                "issuedate": self.Issuedate.get(),
                "expdate": self.ExpDate.get(),
                "dailydose": self.DailyDose.get(),
                "sideEffect": self.sideEffect.get(),
                "furtherInformation": self.furtherInformation.get(),
                "storage": self.StorageAdvice.get(),
                "drivingUsingMachine": self.DrivingUsingMachine.get(),
                "howToUseMedication": self.HowToUseMedication.get(),
                "patientID": self.PatientID.get(),
                "nhsnumber": self.nhsNumber.get(),
                "pname": self.PatientName.get(),
                "dob": self.DateOfBirth.get(),
                "address": self.PatientAddress.get()
            }
            try:
                result = self.collection.update_one({"ref": current_ref}, {"$set": updated_data})

                if result.matched_count > 0:
                    messagebox.showinfo("Başarılı", "Veri başarıyla güncellendi.")
                    self.fetch_data()
                    self.iClear()
                else:
                    messagebox.showerror("Hata", "Güncellenecek kayıt bulunamadı.")
            except Exception as e:
                messagebox.showerror("Hata", f"Veri güncellenirken bir hata oluştu: {e}")
        else:
            messagebox.showinfo("İptal", "Güncelleme iptal edildi.")

    def idelete(self):
        # Seçili hasta verisini MongoDB'den ve Treeview'den siler
        if self.collection is None:
            messagebox.showerror("Hata", "MongoDB bağlantısı kurulamadı. Veri silinemiyor.")
            return

        selected_item = self.hospital_table.focus()
        if not selected_item:
            messagebox.showerror("Hata", "Silinecek bir kayıt seçin.")
            return

        confirm = messagebox.askyesno("Silme Onayı", "Seçilen kaydı silmek istediğinizden emin misiniz?")
        if confirm:
            current_ref = self.ref.get() # Silinecek kaydın referans numarasını al

            try:
                # MongoDB'den referans numarasına göre kaydı sil
                result = self.collection.delete_one({"ref": current_ref})

                if result.deleted_count > 0:
                    messagebox.showinfo("Başarılı", "Kayıt başarıyla silindi.")
                    self.fetch_data() # Verileri güncelledikten sonra Treeview'i yenile
                    self.iClear() # Giriş alanlarını temizle
                else:
                    messagebox.showerror("Hata", "Silinecek kayıt bulunamadı.")
            except Exception as e:
                messagebox.showerror("Hata", f"Kayıt silinirken bir hata oluştu: {e}")
        else:
            messagebox.showinfo("İptal", "Silme işlemi iptal edildi.")

    def iClear(self):
        # Tüm giriş alanlarını ve reçete metnini temizler
        self.NameofTablets.set("İyi") # Varsayılan değeri "İyi" olarak ayarladım
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.furtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hastane Yönetim Sistemi", "Çıkış yapmak istediğinizden emin misiniz?")
        if iExit > 0:
            self.root.destroy()
            return

    def fetch_data(self):
        if self.collection is None:
            messagebox.showerror("Hata", "MongoDB bağlantısı kurulamadı. Veriler çekilemiyor.")
            return

        for item in self.hospital_table.get_children():
            self.hospital_table.delete(item)

        try:
            for record in self.collection.find():

                self.hospital_table.insert("", END, values=(
                    record.get("nameoftablet", ""),
                    record.get("ref", ""),
                    record.get("dose", ""),
                    record.get("nooftablets", ""),
                    record.get("lot", ""),
                    record.get("issuedate", ""),
                    record.get("expdate", ""),
                    record.get("dailydose", ""),
                    record.get("storage", ""),
                    record.get("nhsnumber", ""),
                    record.get("pname", ""),
                    record.get("dob", ""),
                    record.get("address", ""),
                    record.get("sideEffect", ""),
                    record.get("furtherInformation", ""),
                    record.get("drivingUsingMachine", ""),
                    record.get("howToUseMedication", ""),
                    record.get("patientID", "")
                ))
        except Exception as e:
            messagebox.showerror("Hata", f"Veriler çekilirken bir hata oluştu: {e}")

if __name__ == '__main__':
    root = Tk()
    ob = Hospital(root)
    root.mainloop()