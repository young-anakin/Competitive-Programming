class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # self.count = 0
        self.time = {}
        self.timeToLive = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.time[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.time:
            if self.time[tokenId] + self.timeToLive > currentTime:
                self.time[tokenId] = currentTime
            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, values in self.time.items():
            if values + self.timeToLive > currentTime:
                count += 1
        return count
            


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)