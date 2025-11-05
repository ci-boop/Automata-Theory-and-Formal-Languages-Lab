#Mealy Machine
<img width="795" height="611" alt="Screenshot (266)" src="https://github.com/user-attachments/assets/3da3dedf-1b53-4ca3-a736-0fc0766972ef" />
digraph MealyMachine {
    rankdir=LR;
    node [shape = circle];

    // Define States
    A [label="A"];
    B [label="B"];
    C [label="C"];
    D [label="D"];
    E [label="E"];

    // Initial state A
    I [shape = none, label = ""];
    I -> A;

    // Transitions: format "Input/Output"
    A -> A [label="0/A"];
    A -> B [label="1/B"];
    
    B -> C [label="0/A"];
    B -> D [label="1/B"];
    
    C -> D [label="0/C"];
    C -> B [label="1/B"];
    
    D -> B [label="0/B"];
    D -> C [label="1/C"];
    
    E -> D [label="0/C"];
    E -> E [label="1/C"];
}

#Converted Machine
<img width="1007" height="733" alt="Screenshot (267)" src="https://github.com/user-attachments/assets/f84564ad-9e32-443f-8055-d5e1b924aa6c" />
digraph MooreMachine {
    rankdir=LR;
    node [shape = circle];
    
    // Define States and their Outputs (State/Output)
    // Note: States are named (OldState_Output) for clarity but labeled (OldState/Output)
    A_A [label="A/A"];
    B_B [label="B/B"];
    C_A [label="C/A"];
    D_B [label="D/B"];
    D_C [label="D/C"];
    C_C [label="C/C"];
    E_C [label="E/C"];
    
    // Initial State (Assuming A_A is the start state)
    I [shape = none, label = ""];
    I -> A_A;

    // Transitions: CurrentState -> NextState [label="Input"]
    // A_A transitions
    A_A -> A_A [label="0"];
    A_A -> B_B [label="1"];
    
    // B_B transitions
    B_B -> C_A [label="0"];
    B_B -> D_B [label="1"];
    
    // C_A transitions
    C_A -> D_C [label="0"];
    C_A -> B_B [label="1"];
    
    // D_B transitions
    D_B -> B_B [label="0"];
    D_B -> C_C [label="1"];
    
    // D_C transitions
    D_C -> B_B [label="0"];
    D_C -> C_C [label="1"];
    
    // C_C transitions
    C_C -> D_C [label="0"];
    C_C -> B_B [label="1"];

    // E_C transitions
    E_C -> D_C [label="0"];
    E_C -> E_C [label="1"];
}
