class Movie:
    def __init__(self, title, time):
        self.title = title
        self.time = time
        self.seats = [False] * 10

    def reserve_seat(self, seat_number):
        if 0 <= seat_number < len(self.seats):
            if not self.seats[seat_number]:
                self.seats[seat_number] = True
                print(f"좌석 {seat_number} 예약 완료")
            else:
                print("이미 예약된 좌석입니다.")
        else:
            print("유효하지 않은 좌석 번호입니다.")

    def get_available_seats(self):
        return self.seats.count(False)


class Theater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, time):
        if (title, time) not in self.movies:
            self.movies[(title, time)] = Movie(title, time)

    def reserve_movie_seat(self, title, time, seat_number):
        if (title, time) in self.movies:
            self.movies[(title, time)].reserve_seat(seat_number)
        else:
            print("영화 또는 상영 시간이 존재하지 않습니다.")

    def get_movie_schedule(self):
        return list(self.movies.keys())

    def get_available_seats(self, title, time):
        if (title, time) in self.movies:
            return self.movies[(title, time)].get_available_seats()
        else:
            print("영화 또는 상영 시간이 존재하지 않습니다.")
            return None




