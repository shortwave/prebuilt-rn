import 'react-native/Libraries/Core/InitializeCore';
import React from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View
} from 'react-native';


AppRegistry.registerComponent('HelloWorld', () => {
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#FFFFFF'
    },
    title: {
      fontSize: 20,
      textAlign: 'center',
    },
  });
  return () => {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>
          Hello, World!
        </Text>
      </View>
    );
  };

});
