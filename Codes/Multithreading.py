import threading
import time

class TicketBooking:
    def __init__(self):
        self.available = 10
        self.lock = threading.Lock()

    def book_ticket(self, pname, tno):
        #Lock - Book - Unlock
        self.lock.acquire()

        if self.available >= tno:
            print()
            print(pname, "is booking",tno,"tickets.")
            time.sleep(1)
            self.available -= tno
            print(tno,"tickets booked successfully for",pname)
        else:
            print("\nSorry",pname,",",tno,"Tickets not Available!")

        self.lock.release()

if __name__ == "__main__":
    bktk = TicketBooking()
    print("Tickets Available :",bktk.available)

    passengers = [("P1", 8), ("P2", 2), ("P3", 5)]
    threads = []
    for pname, tno in passengers:
        thread = threading.Thread(target=bktk.book_ticket, args=(pname, tno))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nTickets Left :",bktk.available)
    print("\nTickets Booked Successfully!")
