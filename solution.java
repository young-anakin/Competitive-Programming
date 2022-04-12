import java.util.ArrayList;
import java.util.List;

public class solution {

        public List<String> fizzBuzz(int n) {
            List<String> stringArray = new ArrayList<>();
            for(int i =1; i<= n;i++)
            {
                String x = String.valueOf(i);
                if ( i%5 ==0 && i%3 == 0)
                {
                   stringArray.add("FizzBuzz");
                }
                else if(i%3 == 0)
                {
                    stringArray.add("Fizz");
                }
                else if(i%5 == 0) {
                    stringArray.add("Buzz");
                }
                else
                    stringArray.add(x);
            }
            return stringArray;
        }
    }

