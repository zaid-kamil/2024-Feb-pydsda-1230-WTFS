contacts = {
    'police':112,
    'hostpital':102,
}

while True:
    name = input("🔍Search contact: ")
    if len(name) == 0:
        print("👋 Sayonara")
        break
    if name in contacts:
        print(f"📞 {name}: {contacts[name]}")
    elif name == 'all':
        for name, number in contacts.items():
            print(f"📞 {name}: {number}")
        print('-'*20)
    else:
        print(f"🚫 {name} not found")
        ch = input("🤔 Want to add contact? (y/n): ")
        if ch == 'y':
            number = input("📞 Enter number: ")
            contacts[name] = number
            print(f"👍 {name} added to contacts")
            print('-'*20)