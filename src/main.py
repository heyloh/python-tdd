from auction import *

loh = User('Loh')
tauri = User('Tauri')

tauri_bid = Bid(tauri, 100.0)
loh_bid = Bid(loh, 150.0)

auction = Auction('Arranhador')

auction.propose(tauri_bid)
auction.propose(loh_bid)

for bid in auction.bids:
    print(f'The user {bid.user.name} had propose a bid of R${bid.value}.')

print(f'The lowest bid was R${auction.lowest_bid:.2f} and the highest bid was R${auction.highest_bid:.2f}')
