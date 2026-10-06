def initialize_users():
    return {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5"
    }

def add_user(users, username, password):
    # 1. Kullanıcı halihazırda var mı kontrol et
    if username in users:
        return "Bu girişe sahip bir kullanıcı zaten mevcut."
    
    # 2. Yeni kullanıcıyı sözlüğe ekle
    users[username] = password
    return f"Yeni kullanıcı {username} başarıyla eklendi."

def main():
    users = initialize_users()
    print("Sistemde halihazırda kayıtlı kullanıcılar ve şifreleri:")
    for user, pwd in users.items():
        print(f"Kullanıcı adı: {user}, Şifre: {pwd}")
    
    print("\nYeni bir kullanıcı ekleyebilirsiniz.")
    new_username = input("Yeni kullanıcı adını girin: ")
    new_password = input("Yeni kullanıcının şifresini girin: ")
    
    message = add_user(users, new_username, new_password)
    print(message)

if __name__ == "__main__":
    main()