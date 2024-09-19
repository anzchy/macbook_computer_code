chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'getRegex') {
    chrome.storage.local.get(['openaiApiKey'], function(result) {
      if (!result.openaiApiKey) {
        sendResponse({error: 'API key not found. Please set your OpenAI API key.'});
        return;
      }

      const prompt = `
        You are a Regular Expression Guru with the following capabilities:
        1. You excel at all rules and usages of regular expressions covering different flavors, including Python, Perl, JavaScript, .NET, Ruby, and others.
        2. You can tell the difference between flavor-specific features.
        3. For each user question, you will provide at least three useful examples to demonstrate how the regex pattern is used. The default flavor is Python, but if there are no applicable rules in Python or if there's a simpler solution in another flavor, you can provide that as well. Always specify the flavor being used.
        4. You will explain to the user what each character in the pattern string means.

        Given the following description, provide a regex pattern that accomplishes the task:
        
        ${request.input}
        
        Respond with a JSON object containing the following properties:
        1. 'regex': the primary regex pattern (preferably in Python unless specified otherwise)
        2. 'explanation': a detailed explanation of how the regex works, including what each character means
        3. 'examples': an array of at least three objects, each containing:
           - 'flavor': the regex flavor used (e.g., 'Python', 'JavaScript', etc.)
           - 'pattern': the regex pattern for this example
           - 'sample': a sample string that demonstrates the pattern in use
           - 'description': a brief description of what this example does
      `;

      fetchFromOpenAI(result.openaiApiKey, prompt)
        .then(response => {
          try {
            const parsedResponse = JSON.parse(response);
            sendResponse(parsedResponse);
          } catch (error) {
            sendResponse({error: 'Error parsing OpenAI response: ' + error.message});
          }
        })
        .catch(error => {
          sendResponse({error: 'Error fetching from OpenAI: ' + error.message});
        });
    });

    return true; // Indicates that the response will be sent asynchronously
  }
});

function fetchFromOpenAI(apiKey, prompt) {
  return fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: 'You are a regex expert assistant.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      max_tokens: 500
    })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    if (data.choices && data.choices.length > 0) {
      return data.choices[0].message.content;
    } else {
      throw new Error('No response from OpenAI');
    }
  });
}
