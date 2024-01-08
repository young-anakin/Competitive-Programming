from collections import defaultdict
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.stepCount = 0
        self.initial = [width, height]
        self.perimeter = (width-1) * 2 + (height-1)*2
        self.vals = defaultdict(str)
        self.opp = defaultdict(list)
        i = 0
        self.vals[0] = "South"
        self.opp[0] = [0,0] 
        for a in range(1,width):
            i+=1
            self.vals[i] = "East"
            self.opp[i] = [a,0]
        for a in range(1, height):
            i+=1
            self.vals[i] = "North"
            self.opp[i] = [width-1,a]
        a = width-2
        while a >= 0:
            i+=1
            self.vals[i] = "West"
            self.opp[i] = [a, height-1]
            a-=1
        a = height-2
        while a>=0:
            i+=1
            self.vals[i] = "South"
            self.opp[i] = [0,a]
            a-=1
        print(self.vals)
        print(self.opp)
        

    def step(self, num: int) -> None:
        self.stepCount +=num
    def getPos(self) -> List[int]:
        val = self.stepCount % self.perimeter
        return self.opp[val]            
    def getDir(self) -> str:
        fir = bool(self.stepCount//self.perimeter)
        val = self.stepCount % self.perimeter
        if fir:
            return self.vals[val]
        elif not(fir):
            if val == 0:
                return "East"
        return self.vals[val]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()