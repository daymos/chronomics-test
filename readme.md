## Answers

#What are the limitation/problems with this solution?
This solution loads the data in memory. So it only works for exploratory work on the dataset.

# How would it scale?
This can scale a little bit. Afterall, Pandas dataframe are uses with larger dataset then the one provided, however it should not be used for production. Since the task of the assignment is to search the records to match a query, the optimal answer is to store the data into a database. 
The question is then how to add the data into the database, starting from these VCF file format. The library I used support HDF5. Using HDF5 the data is stored in the Filesystem rathern then in memory. Accessing the data is done in chunks ( handled by the library) and should never tax the memory of the machine.
For proper scaling I would write a consumer that read the VCF files into local HDF5, then vaildates the fields and finally store them into a database. Then the search query can be delegated to the DB. 

# How would you test it efficiently?  
I split the operations into the smallest function possible, so that it can be unit tested.
Because there is not so much logic, unit test is potentially not particularly usefull, and instead I would add some data type validation. 
In a production scenario, where the data would be stored in a database, I would create a class called for example "Record", with some strong validation methods for each field, for example using something like Pydantic.
In this way the data is wrapped inside the record class, and every function that process Record has to comply with it. The issue at that point becomes to keep the validation methods up to date with the database schema.
