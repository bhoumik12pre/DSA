#include <iostream>
#include <string>
using namespace std;

const int MAX_CITIES = 20;

struct Node {
    string vertex;
    int time;
    Node* next;
};

class AdjMatList {
private:
    int adjacencyMatrix[MAX_CITIES][MAX_CITIES];
    string cities[MAX_CITIES];
    Node* head[MAX_CITIES];

public:
    AdjMatList() {
        for (int i = 0; i < MAX_CITIES; ++i)
            head[i] = nullptr;
    }

    void createGraph();
    void displayAdjacencyMatrix();
    void displayAdjacencyList();
};

void AdjMatList::createGraph() {
    int n;
    cout << "\nEnter the number of cities (max. " << MAX_CITIES << "): ";
    cin >> n;
    if (n <= 0 || n > MAX_CITIES) {
        cout << "Invalid number of cities.\n";
        return;
    }

    cout << "\nEnter the names of cities:\n";
    for (int i = 0; i < n; ++i)
        cin >> cities[i];

    cout << "\nInput whether there is a path between each pair of cities (y/n):\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char ch;
            cout << "\nIs there a path between " << cities[i] << " and " << cities[j] << "? (y/n): ";
            cin >> ch;
            if (ch == 'y') {
                cout << "Enter time required to reach " << cities[j] << " from " << cities[i] << " in minutes: ";
                cin >> adjacencyMatrix[i][j];
            } else {
                adjacencyMatrix[i][j] = 0;
            }
        }
    }

    cout << "\nGraph created successfully.\n";
}

void AdjMatList::displayAdjacencyMatrix() {
    cout << "\nAdjacency Matrix:\n";
    cout << "\t";
    for (int j = 0; j < MAX_CITIES; ++j)
        cout << cities[j] << "\t";
    cout << endl;
    for (int i = 0; i < MAX_CITIES; ++i) {
        cout << cities[i] << "\t";
        for (int j = 0; j < MAX_CITIES; ++j)
            cout << adjacencyMatrix[i][j] << "\t";
        cout << endl;
    }
}

void AdjMatList::displayAdjacencyList() {
    cout << "\nAdjacency List:\n";
    for (int i = 0; i < MAX_CITIES; ++i) {
        if (head[i] == nullptr) {
            cout << "Adjacency list not present\n";
            break;
        } else {
            cout << cities[i] << ":";
            Node* temp = head[i];
            while (temp != nullptr) {
                cout << " -> " << temp->vertex << " [time required: " << temp->time << " min]";
                temp = temp->next;
            }
            cout << endl;
        }
    }
}

int main() {
    AdjMatList a;
    while (true) {
        cout << "\n\nEnter the choice\n";
        cout << "1. Enter graph\n";
        cout << "2. Display adjacency matrix for cities\n";
        cout << "3. Display adjacency list for cities\n";
        cout << "4. Exit\n";

        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                a.createGraph();
                break;
            case 2:
                a.displayAdjacencyMatrix();
                break;
            case 3:
                a.displayAdjacencyList();
                break;
            case 4:
                exit(0);
            default:
                cout << "\nUnknown choice\n";
        }
    }
    return 0;
}
