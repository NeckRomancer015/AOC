import re
import math

class retrieve_numbers:
    def get_first_and_last_number(line:str)->list[str]:
        """
        Gets first and last numbers, includes written numbers as well.

        Parameters
        ----------
        str
            a line of input

        Returns
        -------
        list[str]
            A list containing 2 numbers as strings
            If only 1 number present, second word returned as None
        Example
        -------
        >>> get_first_and_last_number('agdaone2three4afour5')
        ['1', '5']
        """
        numbers = {'one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
        first_word,second_word = None,None
        tmp=''
        for i in line:
            if i.isnumeric():
                tmp=''
                if first_word:
                    second_word= i
                else:
                    first_word=i
            else:
                tmp+=i
                for num in numbers.keys():
                    if num in tmp:
                        if first_word:
                            second_word = numbers.get(num)
                        else:
                            first_word = numbers.get(num)
                        tmp = tmp[-1] # twone sevenine fiveight nineight oneight eighthree threeight
                        break
        
        return [first_word,second_word]
    
    def get_numbers_as_string(line:str)->str:
        """
        Returns all the numbers in a string.

        Parameters
        ----------
        line : str
            The line containing numbers and other characters.
        

        Returns
        -------
        str
            A string containing all the numbers in the order they appeared.

        Examples
        --------
        >>> get_numbers_as_string('asf4a54faa7')
        '4547'
        """
        return "".join(re.findall(r'\d+',line))
    
    def get_numbers_as_string(line:str)->str:
        """
        Returns all the numbers in a string.

        Parameters
        ----------
        line : str
            The line containing numbers and other characters.
        

        Returns
        -------
        str
            A string containing all the numbers in the order they appeared.

        Examples
        --------
        >>> get_numbers_as_string('asf4a54faa7')
        '4547'
        """
        return "".join(re.findall(r'\d+',line))

    def get_numbers_as_list(line:str)->list[str]:
        """
        Returns all the numbers in a string.

        Parameters
        ----------
        line : str
            The line containing numbers and other characters.
        

        Returns
        -------
        list[str]
            A list containing all the numbers stored as strings in the order they appeared.

        Examples
        --------
        >>> get_numbers_as_list('as5a5ff6')
        ['5', '5', '6']
        """
        return re.findall(r'\d+',line)

    def get_numbers_as_int_in_list(line:str)->list[int]:
        """
        Returns all the numbers in a string.

        Parameters
        ----------
        line : str
            The line containing numbers and other characters.
        

        Returns
        -------
        list[int]
            A list containing all the numbers stored as ints in the order they appeared.

        Examples
        --------
        >>> get_numbers_as_int_in_list('as5a5ff6')
        [5, 5, 6]
        """
        return [int(x) for x in re.findall(r'\d+',line)]


    def get_first_and_last_numbers_in_string_as_list(line:str)->list[str]:
        """
        Returns the first and last numbers in a list as a list

        Parameters
        ----------
        line: str

        Returns
        -------
        list[str]
            Returns a list containing the first and last number 

        Examples
        --------
        >>> get_first_and_last_numbers_in_string_as_list('as8faqer5ffsa84a')
        ['8','84']
        """
        numbers = re.findall(r'\d+',line)
        return [numbers[0],numbers[-1]]

    def get_first_and_last_numbers_in_list_as_list(l:list[str])->list[str]:
        """
        Returns the first and last numbers in a string as a list

        Parameters
        ----------
        array: list[str]

        Returns
        -------
        list[str]
            Returns a list containing the first and last number 

        Examples
        --------
        >>> get_first_and_last_numbers_in_list_as_list('as8faqer5ffsa84a')
        ['8', '84']
        """
        return retrieve_numbers.get_first_and_last_numbers_in_string_as_list("".join(l))

def read_file_line_by_line(file_path:str):
    """
    Reads a file line by line and yields each line.

    Args:
        file_path (str): The path to the file to be read.

    Yields:
        str: The next line in the file.

    Example:
        >>> for line in read_file_line_by_line("example.txt"):
        >>>     print(line)
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")
    
def create_deck_of_card()->list[str]:
    """
    Creates a deck of cards

    Parameters
    ----------
    None

    Returns
    -------
    list[str]
        A list containing strings which represent each card of the deck

    Example
    -------
    >>> create_deck_of_card()
    ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
    """
    cards = []
    for s in ['H','C','D','S']:
        for i in range(2,11):
            cards.append(str(i)+s)
        for p in ['J','Q','K','A']:
            cards.append(p+s)
    return cards


class math_functions:
    def lcm(a, b):
        """
        Returns lowest common multipler.

        Parameters
        ----------
        int,int
            Two numbers
        
        Returns
        -------
        int
            returns the lcm
        
        Example
        -------
        >>> lcm(5,15)
        15
        """
        return a * b // math.gcd(a, b)

    def is_points_diagonal(x1:int,x2:int,y1:int,y2:int):
        """
        Determines if 2 coordinates are diagonal

        Parameters
        ----------
        int,int,int,int
            x1,y1,x2,y2
        
        Returns
        -------
        bool
            returns True if they are diagonal, else False
        
        Example
        -------
        >>> is_points_diagonal(8,0,0,8)
        True
        """
        return abs(x1-x2) == abs(y1-y2)

    def manhattan_distance(x1:int, y1:int, x2:int, y2:int)->int:
        """
        Returns the manhattan distance for 2 coordinates.

        Parameters
        ----------
        int,int,int,int
            x1,y1,x2,y2
        
        Returns
        -------
        int
            returns the manhattan distance
        
        Example
        -------
        >>> manhattan_distance(0,1,1,2)
        2
        """
        return abs(x1 - x2) + abs(y1 - y2)

    def get_diagonal_points(x1, y1,x2,y2, do_validation = False):
        """
        Get all integer points between two diagonal coordinates (inclusive).

        Parameters
        -----------
        x1,y1,x2,y2

        Returns
        --------
        list[tuple]
            List of points between p1 and p2, including both endpoints.
        
        Example
        -------
        >>> get_diagonal_points(0,3,3,0)
        [(0, 3), (1, 2), (2, 1), (3, 0)]
        """
        if do_validation:
            if abs(x2 - x1) != abs(y2 - y1):
                raise ValueError("The points are not diagonal.")
            
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1

        points = []
        x, y = x1, y1
        while (x, y) != (x2, y2):
            points.append((x, y))
            x += dx
            y += dy
        points.append((x2, y2))
        return points

    def get_neighbors(x, y):
        offsets = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1), (1, 0), (1, 1)]
        # Compute neighbors
        neighbors = [(x + dx, y + dy) for dx, dy in offsets]

        #Use the below to check if the coords are valid in a grid
        # 0<=x<len(grid) and 0<=y<len(grid[r])
        return neighbors

    def get_diagonal_neighbors(x, y):
        # Define relative positions for diagonal neighbors
        offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        # Compute diagonal neighbors
        neighbors = [(x + dx, y + dy) for dx, dy in offsets]
        return neighbors
    
    def find_factors_optimized(number:int):
        """
        Finds and returns the factors of a given number using an optimized approach.
        """
        factors = set()  # Use a set to automatically handle duplicates and maintain uniqueness
        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                factors.add(i)
                factors.add(number // i)
        return sorted(list(factors)) 
    
if __name__ == '__main__':
    print(math_functions.find_factors_optimized(10))