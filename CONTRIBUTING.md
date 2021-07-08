# Contributing to Tabby

## Styleguides

### Git Commit Messages

- Use present tense ("add" not "added")
- Use imperative mood ("add" not "adds")
- Begin the title with a type and scope marker, i.e.
  `<type>(<scope>): <description>` using one of the following types:
  - `docs` for documentation (both embedded in code and separate files).
  - `feat` for adding a feature
  - `fix` for addressing issues, fixing bugs
  - `refactor` for rewriting existing features
  - `style` for fixing linting issues and other formatting errors
  - `infra` for adding boilerplate, importing libraries, or setting up CI and
    the like
- Keep the scope succinct, most updates should fall into one of these scopes:
  - `route` for URL routing
  - `model` for changes to the database models
  - `view` for view rendering and middleware directly connected to it
  - `ctrl` for controller functionality
  - `style` for updating CSS or adding images

### Python Styleguide

All Python code is linted with YAPF, see [.style.yapf](/.style.yapf) for the
exact settings. To enable auto-formatting in VS Code, install the
`ms-python.python` extension and change the `Python > Formatting: Provider`
setting to `yapf`.

1. Top level definitions should be divided by only a single line.

   ```python
   # Bad
   def foo():
   print('foo!')


   def bar():
     print('bar!')

   # Good
   def foo():
   print('foo!')

   def bar():
     print('bar!')
   ```

2. Braces should be coalesced to keep from making files unnecessarily vertical:

   ```python
   # Bad
   takes_a_dict(
     {
       'key_1': 'value_1',
       'key_2': 'value_2'
     }
   )

   # Good
   takes_a_dict({
     'key_1': 'value_1',
     'key_2': 'value_2'
   })
   ```

3. All lines should be limited to 80 columns wide. This can be visually
   indicated in VS Code by adding the following to your workspace or user
   `settings.json` file:

   ```json
   "editor.rulers": [ 80 ],
   ```

4. Closing braces should "dedent", i.e. be on the same column as the beginning
   of the line where the brace was opened:

   ```python
   # Bad
   some_dict = {
     'key_1': 'value_1',
     'key_2': 'value_2'
     }

   # Good
   some_dict = {
     'key_1': 'value_1',
     'key_2': 'value_2'
   }
   ```

5. Indentation should be done with 2 spaces:

   ```python
   # Bad
   if foo:
       bar()

   # Good
   if foo:
     bar()
   ```

6. All control blocks should be spread out into separate lines, not joined:

   ```python
   # Bad
   if foo: bar()

   # Good
   if foo:
     bar()
   ```

7. Comments following code lines should be tabbed to multiples of 8 for
   consistency and readability (i.e. starting on column 16, 24, 32, etc.)

   ```python
   # Bad
   colors = ('red', 'green', 'blue') # Define colors tuple
   print(len(colors))  # Use len() to get count

   # Good
   colors = ('red', 'green', 'blue')      # Define colors tuple
   print(len(colors))                     # Use len() to get count
   ```
