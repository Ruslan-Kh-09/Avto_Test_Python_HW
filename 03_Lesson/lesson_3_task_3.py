from address import Address
from mailing import Mailing

address_to = Address("296000", "Черкесск", "Фрунзе", "2", "22")

address_from = Address("369000", "Ставрополь", "Мира", "22", "71")

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=888.99,
    track="RU123456789CN"
)

from_addr = my_mailing.from_address
to_addr = my_mailing.to_address


def format_address(addr):

    return (f"{addr.index}, {addr.city}, {addr.street}, "
            f"{addr.house} - {addr.apartment}")


print(f"Отправление {my_mailing.track}"
      f" из {format_address(from_addr)}"
      f" в {format_address(to_addr)}."
      f" Стоимость {my_mailing.cost} рублей.")

