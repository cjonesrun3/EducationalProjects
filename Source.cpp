/*
This is code for a two player dice game. It simulates rolling 5 dice, appending the result to a vector, then repeating that for ten rounds.
At the end, we iterate through and compare rounds to see which player has won the round. 
/**/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	vector<int> playerOne;
	vector<int> playerTwo;

	cout << "Welcome to the dice game!\n" << endl;

	string playerOneName;
	cout << "Enter player 1's name: ";
	getline(cin, playerOneName);

	string playerTwoName;
	cout << "Enter player 2's name: ";
	getline(cin, playerTwoName);

	cout << "Welcome " << playerOneName << " and " << playerTwoName << endl;

	int roundCounter = 0;

	while (roundCounter < 11)
	{
		int playerOneRoll = rand() % 30 + 1;  // Generates a random number between 1-30
		int playerTwoRoll = rand() % 30 + 1;

		playerOne.push_back(playerOneRoll);  // Pushes players rolls to vector
		playerTwo.push_back(playerTwoRoll);

		++roundCounter;  // Add one to round counter

	}

	for (int i = 0; i < playerOne.size(); ++i)  // Iterates through playerOne's vector and rolls for each round
	{
		for (int a = 0; a < playerTwo.size(); ++a)  // Iterates through playerTwo's vector and rolls for each round
		{
			if (i = a) // compares rolls by index within the vectors
			{
				if (playerOne[i] > playerTwo[a])  // Player 1 victory condition
				{
					cout << "Round: " << i << " Player 1 Wins! with " << playerOne[i] << " Over " << playerTwo[a] << endl;
					
				}
				else if (playerTwo[a] > playerOne[i])  // Player 2 victory condition
				{
					cout << "Round: " << a << " Player 2 Wins! with " << playerTwo[a] << " Over " << playerOne[i] << endl;
					
				}
				else  // Tie condition
				{
					cout << "Round: " << i << " Was a tie!" << endl;
					
				}
			}
		}
	}

	

	

}
