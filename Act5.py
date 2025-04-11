class FreelanceJob():
    def __init__(self, client_name, job_title):
        self.client_name = client_name
        self.job_title = job_title

    def calculate_earnings(self):
        pass

    def describe_job(self):
        return f"Job: {self.job_title} for {self.client_name}"
   
class Mcdonalds(FreelanceJob):
    def __init__(self, client_name, job_title, hourly_rate, hours_worked):
        super().__init__(client_name, job_title)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_earnings(self):
        return (self.hourly_rate * self.hours_worked)

    def describe_job(self):
        return f"Mcdonald's employee: {self.job_title} for {self.client_name}, {self.hours_worked} hours at ₱{self.hourly_rate:.2f} per hour."
       
class Photographer(FreelanceJob):
   
    def __init__(self, client_name, job_title, hourly_rate, hours_worked, bonus=0):
        super().__init__(client_name, job_title)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus = bonus

    def calculate_earnings(self):
        return (self.hourly_rate * self.hours_worked) + self.bonus
   
    def describe_job(self):
        description = f"Photograpy job: {self.job_title} for {self.client_name}, {self.hours_worked} hours at ₱{self.hourly_rate:.2f} per commission"
        if self.bonus > 0:
            description += f" + ₱{self.bonus:.2f} bonus"
            return description + "."
       
class DeliveryDriver(FreelanceJob):
    def __init__(self, client_name, job_title, hourly_rate, hours_worked):
        super().__init__(client_name, job_title)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_earnings(self):
        return (self.hourly_rate * self.hours_worked)
   
    def describe_job(self):
        return f"Mcdonald's employee: {self.job_title} for {self.client_name}, {self.hours_worked} hours at ${self.hourly_rate:.2f} per hour."

   
def generate_invoice(job_list):
        print("---Freelance Job Invoice---")
        for job in job_list:
            earnings = job.calculate_earnings()
            print(f"Client: {job.client_name}")
            print(f"Job Title: {job.job_title}")
            print(f"Earnings: ${earnings:.2f}")
            if hasattr(job, 'describe_job'):
                print(f"Description: {job.describe_job()}")
                print("-" * 20)


job1 = Mcdonalds("Mcdonald's", "Cashier", 1200, 20)
job2 = Photographer("E-Commerce Platform", "Photograpy", 40, 15, bonus=500)
job3 = DeliveryDriver("Marketing", 40, 6000, 600)

job_list = [job1, job2, job3]
generate_invoice(job_list)