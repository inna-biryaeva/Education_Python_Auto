from address import Address
from mailing import Mailing
to_ad = Address("197374", "Saint Petersburg", "Savushkina street", "126", "27")
from_ad = Address("125424", "Moscow", "Volokolamskoye highway", "69", "2")
mail = Mailing(to_address=to_ad, from_address=from_ad, cost=7, track="RFPL20262027")
print(f"Отправление {mail.track} "
      f"из {mail.from_address.postal_code}, "
      f"{mail.from_address.city}, ",
      f"{mail.from_address.street}, ",
      f"{mail.from_address.building} - "
      f"{mail.from_address.apartment} "
      f"в {mail.to_address.postal_code}, "
      f"{mail.to_address.city}, "
      f"{mail.to_address.street}, "
      f"{mail.to_address.building} - "
      f"{mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей."
      )
