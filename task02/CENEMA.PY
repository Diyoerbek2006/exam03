class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False


class Ticket:
    def __init__(self, seat: Seat, owner: str):
        if not isinstance(seat, Seat):
            raise ValueError(" Seat class obyekti bo'lishi kerak")
        if not owner.strip():
            raise ValueError("EGA bo'sh bo'lishi mumkin emas")
        self.seat = seat
        self.owner = owner


class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if not movie_title.strip():
            raise ValueError("movie title bo'sh bo'lishi mumkin emas")
        if not isinstance(total_seats, int) or total_seats <= 0:
            raise ValueError("total seats 0 dan katta bo'lishi kerak")

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []

    def available_seats(self) -> list[int]:
        return [seat.number for seat in self.seats if not seat.is_taken]

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError(f"O'rin raqami 1 dan {self.total_seats} gacha bo'lishi kerak")

        seat = self.seats[seat_number - 1]
        if seat.is_taken:
            raise RuntimeError(f"O'rin {seat_number} allaqachon bron qilingan")

        seat.is_taken = True
        ticket = Ticket(seat, user)
        self.bookings.append(ticket)
        return ticket

    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"


if __name__ == "__main__":
    session = CinemaSession("Avatar 2", 5)

    print("Bo'sh o'rinlar:", session.available_seats())  

    ticket1 = session.book_seat(3, "Ali")
    ticket2 = session.book_seat(1, "Vali")

    print("Bo'sh o'rinlar:", session.available_seats())  

    try:
        session.book_seat(3, "Sardor")
    except RuntimeError as e:
        print("Xato:", e)

    print(f"Jami bron: {len(session.bookings)}")
    for ticket in session.bookings:
        print(f"O'rin {ticket.seat.number}: {ticket.owner}")

    print(session)  
